from flask import Blueprint, request
from marshmallow import ValidationError
from app.services import MovimientoService, StockService, ResponseBuilder, InsufficientStockException, StockBlockException
from ..mapping import MovimientoSchema, StockSchema, ResponseSchema
from app import db

response_schema = ResponseSchema()
stock_schema = StockSchema()
movimiento_schema = MovimientoSchema()

movimiento_service = MovimientoService()
stock_service = StockService()

inventario = Blueprint('inventario', __name__)

@inventario.route('/', methods=['GET'])
def index():
    db.create_all()
    return 'hola mundo', 200

@inventario.route('/inventario', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    try:
        movimiento = movimiento_schema.load(request.json)
        data = movimiento_schema.dump(movimiento_service.add(movimiento))
        response_builder.add_message("Inventario added").add_status_code(201).add_data(data)
        return response_schema.dump(response_builder.build()), 201
    
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422
    
    except InsufficientStockException as err:
        response_builder.add_message(str(err)).add_status_code(400).add_data({})
        return response_schema.dump(response_builder.build()), 400
    
    except StockBlockException as err:
        response_builder.add_message(str(err)).add_status_code(423).add_data({})
        return response_schema.dump(response_builder.build()), 423


@inventario.route('/inventario', methods=['GET'])
def get_all():
    response_builder = ResponseBuilder()
    data = stock_schema.dump(stock_service.all(), many=True)
    response_builder.add_message("Inventario found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@inventario.route('/inventario/movimientos', methods=['GET'])
def get_movimientos():
    response_builder = ResponseBuilder()
    data = movimiento_schema.dump(movimiento_service.all(), many=True)
    response_builder.add_message("Movimientos found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@inventario.route('/inventario/<int:id>', methods=['GET'])
def get_cuantity(id):
    message = "No existe el producto"
    code = 404
    response_builder = ResponseBuilder()
    cuantity = stock_service.cuantity(id)
    if cuantity is not None:
        response_builder.add_message("Cuantity found").add_status_code(200).add_data(cuantity)
        return response_schema.dump(response_builder.build()), 200
    response_builder.add_message(message).add_status_code(code).add_data({'id': id})
    return response_schema.dump(response_builder.build()), code
       