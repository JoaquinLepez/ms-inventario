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

    
    def add(self, stock: Stock) -> Stock:
        repository.add(stock)
        return stock

    def update_cuantity(self, product_id: int, cuantity: int) -> None:
        repository.update_cuantity(product_id, cuantity)

    def delete(self, id: int) -> bool:
        stock = self.find(id)
        if stock:
            cache.delete(f'stock_{stock.id}')
            repository.delete(stock)
            return True
        else: 
            return False
    
    def find_by_product_id(self, product_id: int) -> int:
        cantidad = repository.find_by_product_id(product_id) 
        return cantidad
     

    def get_stock(self, product_id: int) -> int:
        stock = cache.get(f'stock_of_{product_id}')
        if stock is None:
            stock = self.find_by_product_id(product_id)
            if stock is None:
                new_stock = Stock(
                    producto_id = product_id,
                    cantidad = 0
                )
                stock = self.add(new_stock)
            cache.set(f'stock_of_{product_id}', stock, timeout=100)
        return stock
    