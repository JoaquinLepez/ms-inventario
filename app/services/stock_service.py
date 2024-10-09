from ..repository import StockRepository
from app.models import Stock

repository = StockRepository()

class StockService:

    def all(self) -> list[Stock]:
        return repository.all()
    
    def save(self, stock: Stock) -> Stock:
        return repository.save(stock)
    
    def delete(self, id: int) -> bool:
        stock = self.find(id)
        if stock:
            repository.delete(stock)
            return True
        else: 
            return False
    
    def find(self, id: int) -> Stock:
        return repository.find(id)
    