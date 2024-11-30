from app.models import Stock
from marshmallow import fields, Schema, post_load

class StockSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)

    @post_load
    def make_data(self, data, **kwargs):
        return Stock(**data)