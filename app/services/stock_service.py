from app.repositories import StockRepository
from app.models import Stock, Movimiento
from app import cache

repository = StockRepository()

class StockService:

    def all(self) -> list[Stock]:
        result = cache.get('stock')
        if result is None:
            result = repository.all()
            cache.set('stock', result, timeout=15)
        return result
    
    def add(self, movimiento: Movimiento) -> Stock:
        stock = self.find_by_product_id(movimiento.producto_id)
        if stock:
            cantidad = stock.cantidad + (movimiento.entrada_salida * movimiento.cantidad)
            repository.update_cuantity(stock.id, cantidad)
            cache.delete(f'stock_cuantity{stock.producto_id}')
        else:
            stock = Stock(producto_id=movimiento.producto_id, cantidad=movimiento.cantidad)
            repository.add(stock)

        return stock

    def delete(self, id: int) -> bool:
        stock = self.find(id)
        if stock:
            cache.delete(f'stock_{stock.id}')
            repository.delete(stock)
            return True
        else: 
            return False
    
    def find_by_product_id(self, product_id: int) -> Stock:
        return repository.find_by_product_id(product_id)
    
    def cuantity(self, product_id: int) -> int:
        stock = self.find_by_product_id(product_id)
        if stock:
            cantidad = cache.get(f'stock_cuantity{product_id}')
            if cantidad is None:
                cantidad = stock.cantidad
                cache.set(f'stock_cuantity{product_id}', cantidad, timeout=15)
            return cantidad
        else:
            return None

