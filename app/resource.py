from flask import Blueprint, request
from .services import StockService, ResponseBuilder
from .mapping import StockSchema, ResponseSchema

response_schema = ResponseSchema()
stock_service = StockService()
stock_schema = StockSchema()

inventario = Blueprint('inventario', __name__)


@inventario.route('/inventario', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = stock_schema.dump(stock_service.all(), many=True)
    response_builder.add_message("Inventario found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@inventario.route('/inventario', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    stock = stock_schema.load(request.json)
    data = stock_schema.dump(stock_service.save(stock))
    response_builder.add_message("Inventario added").add_status_code(201).add_data(data)
    return response_schema.dump(response_builder.build()), 201

@inventario.route('/inventario/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    data = stock_service.delete(id)
    if data:
        response_builder.add_message("Inventario deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Inventario not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404


