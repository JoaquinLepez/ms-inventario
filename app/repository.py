from typing import List
from app import db
from app.models import Stock

class StockRepository:
    def all(self) -> List[Stock]:
        return db.session.query(Stock).all()
    
    def save(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock
    
    def delete(self, stock: Stock) -> None:
        db.session.delete(stock)
        db.session.commit()
        return None
    
    def find(self, id: int) -> Stock:
        return db.session.query(Stock).filter(Stock.id == id).one_or_none()
        