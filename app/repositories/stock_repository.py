from typing import List
# from sqlalchemy import func
from app import db
from app.models import Stock

class StockRepository:
    def all(self) -> List[Stock]:
        return db.session.query(Stock).all()
    
    def add(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock
    
    def delete(self, stock: Stock) -> None:
        db.session.delete(stock)
        db.session.commit()
        return None
    
    def update_cuantity(self, id: int, cuantity = int) -> None:
        db.session.query(Stock).filter(Stock.id == id).update({'cantidad': cuantity})
        db.session.commit()

    def find_by_product_id(self, product_id: int) -> Stock:
        return db.session.query(Stock).filter(Stock.producto_id == product_id).first()