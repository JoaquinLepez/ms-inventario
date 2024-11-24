from ..repository import StockRepository
from app.models import Stock
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
        stock = repository.add(stock)
        cache.set(f'stock_{stock.id}', stock, timeout=15)
        return stock
    
    def delete(self, id: int) -> bool:
        stock = self.find(id)
        if stock:
            repository.delete(stock)
            return True
        else: 
            return False
    
    def find(self, id: int) -> Stock:
        return repository.find(id)
    