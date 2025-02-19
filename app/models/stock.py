from sqlalchemy import Column, Integer, CheckConstraint
from app import db

class Stock(db.Model):
    __tablename__ = 'stock'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    producto_id: str = db.Column(db.Integer, nullable = False)
    cantidad: int = db.Column(db.Integer, nullable = False)

