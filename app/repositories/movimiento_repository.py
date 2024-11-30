from typing import List
# from sqlalchemy import func
from app import db
from app.models import Movimiento, Stock

class MovimientoRepository:
    def all(self) -> List[Movimiento]:
        return db.session.query(Movimiento).all()
    
    def add(self, movimiento: Movimiento) -> Movimiento:
        db.session.add(movimiento)
        db.session.commit()
        return movimiento
    
    def delete(self, movimiento: Movimiento) -> None:
        db.session.delete(movimiento)
        db.session.commit()
        return None
    
    def delete_all(self) -> None: 
        db.session.execute(Movimiento.__table__.delete())
        db.session.execute(Stock.__table__.delete())
        return None
    
    # def cuantity(self, id: int) -> int:
    #     cantidad = db.session.query(func.sum(Stock.cantidad * Stock.entrada_salida)) \
    #                         .filter(Stock.producto_id == id) \
    #                         .scalar()
    #     return cantidad if cantidad is not None else 0
    
    