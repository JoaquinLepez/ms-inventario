from threading import Lock
from datetime import datetime
from app.repositories import MovimientoRepository
from app.services import StockService
from app.models import Stock, Movimiento
from app import cache
class InsufficientStockException(Exception):
    def __init__(self, message="No hay suficiente stock"):
        self.message = message
        super().__init__(self.message)

repository = MovimientoRepository()
stock = StockService()
lock = Lock()

class MovimientoService:

    def all(self) -> list[Movimiento]:
        result = cache.get('movimientos')
        if result is None:
            result = repository.all()
            cache.set('movimientos', result, timeout=15)
        return result
    
    def add(self, movimiento: Movimiento) -> Movimiento:
        lock.acquire()
        if movimiento.entrada_salida == -1 and stock.cuantity(movimiento.producto_id) < movimiento.cantidad:
            lock.release()    
            raise InsufficientStockException()
        movimiento.fecha_transaccion = datetime.now()
        repository.add(movimiento)
        stock.add(movimiento)
        lock.release()
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