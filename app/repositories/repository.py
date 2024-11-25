from typing import List
from sqlalchemy import func
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
    
    def find(self, id: int) -> Stock:
        return db.session.query(Stock).filter(Stock.id == id).one_or_none()
    
    def cuantity(self, id: int) -> int:
        cantidad = db.session.query(func.sum(Stock.cantidad * Stock.entrada_salida)) \
                            .filter(Stock.producto_id == id) \
                            .scalar()
        return cantidad if cantidad is not None else 0
    
    