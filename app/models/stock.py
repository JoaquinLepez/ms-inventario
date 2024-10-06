from sqlalchemy import Column, Integer, CheckConstraint
from app import db

class Stock(db.Model):
    __tablename__ = 'stock'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    producto_id: str = db.Column(db.Integer, nullable = False)
    fecha_transaccion: str = db.Column(db.DateTime, nullable = False)
    cantidad: int = db.Column(db.Integer, nullable = False)
    entrada_salida: int = db.Column(db.Integer, CheckConstraint('entrada_salida IN (1, 2)'), nullable=False)

