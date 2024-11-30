from app.models import Movimiento
from marshmallow import fields, Schema, post_load, validate

class MovimientoSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_transaccion = fields.DateTime(dump_only=True)
    cantidad = fields.Integer(required=True)
    entrada_salida = fields.Integer(required=True,  validate=validate.OneOf([1, -1]))

    @post_load
    def make_data(self, data, **kwargs):
        return Movimiento(**data)