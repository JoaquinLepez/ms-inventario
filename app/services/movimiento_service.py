from threading import Lock
from datetime import datetime
from app.repositories import MovimientoRepository
from app.services import StockService
from app.models import Stock, Movimiento
from app import cache
import redis

r = redis.Redis(host='redis_ecommerce', port=6379, db=1, password='A123456')
redis_lock = redis.lock.Lock(r,name='Mi_lock', timeout= 10)


class InsufficientStockException(Exception):
    def __init__(self, message="No hay suficiente stock"):
        self.message = message
        super().__init__(self.message)

class StockBlockException(Exception):
    def __init__(self, message="El stock está bloqueado por otro proceso"):
        self.message = message
        super().__init__(self.message)

repository = MovimientoRepository()
stock_service = StockService()
lock = Lock()

class MovimientoService:

    def all(self) -> list[Movimiento]:
        result = cache.get('movimientos')
        if result is None:
            result = repository.all()
            cache.set('movimientos', result, timeout=15)
        return result

    def add(self, movimiento: Movimiento) -> Movimiento:
        redis_lock.acquire(blocking=True)
        lock.acquire()
        stock = stock_service.get_stock(movimiento.producto_id)
        if movimiento.entrada_salida == -1 and stock < movimiento.cantidad:
            lock.release()   
            redis_lock.release() 
            raise InsufficientStockException()
        movimiento.fecha_transaccion = datetime.now()
        repository.add(movimiento)
        new_cuantity = stock + (movimiento.entrada_salida * movimiento.cantidad)
        stock_service.update_cuantity(movimiento.producto_id, new_cuantity)
        cache.set(f'stock_of_{movimiento.producto_id}', new_cuantity, 100)
        lock.release()
        redis_lock.release()
        return movimiento
    
    
    def delete(self, id: int) -> bool:
        movimiento = self.find(id)
        if movimiento:
            repository.delete(movimiento)
            return True
        else: 
            return False
    
    def find(self, id: int) -> Stock:
        return repository.find(id)
    
    def delete_all(self) -> bool:
        repository.delete_all()
        return True