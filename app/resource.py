from flask import Blueprint, request
# from app.mapping import TaskSchema, ResponseSchema, UserSchema
# from app.services.response_message import ResponseBuilder
from .service import StockService

stock_service = StockService()

inventario = Blueprint('inventario', __name__)

# task_schema = TaskSchema()
# user_schema = UserSchema()
# response_schema = ResponseSchema()

# task_service = TaskService()
@inventario.route('/', methods=['GET'])
def index():
    stocks = stock_service.all()
    return stocks, 200

# @producto.route('/productos', methods=['GET'])
# def index():
#     response_builder = ResponseBuilder()
#     data = task_schema.dump(task_service.all(), many=True)
#     response_builder.add_message("Tasks found").add_status_code(200).add_data(data)

#     return response_schema.dump(response_builder.build()), 200
    
# Post: Crea una nueva task a partir de un JSON
# @task.route('/tasks/add', methods=['POST'])
# def add_task():
#     response_builder = ResponseBuilder()
#     task = task_schema.load(request.json)
#     data = task_schema.dump(task_service.save(task))
#     response_builder.add_message("Task created").add_status_code(201).add_data(data)

#     return response_schema.dump(response_builder.build()), 201

# # Delete: Elimina una task a partir de su id
# @task.route('/tasks/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     task_service.delete(id)
#     response_builder = ResponseBuilder()
#     response_builder.add_message("Task deleted").add_status_code(200).add_data({'id': id})
#     return response_schema.dump(response_builder.build()), 200

# # Get: JSON con los datos de la task buscado por id
# @task.route('/tasks/<int:id>', methods=['GET'])
# def find(id):
#     response_builder = ResponseBuilder()
#     data = task_schema.dump(task_service.find(id))
#     if data:
#         response_builder.add_message("Task found").add_status_code(200).add_data(data)
#         return response_schema.dump(response_builder.build()), 200
#     else:
#         response_builder.add_message("Task NOT found").add_status_code(404)
#         return response_schema.dump(response_builder.build()), 404

# # Put: Actualiza una task a partir de un JSON
# @task.route('/tasks/<int:id>', methods=['PUT'])
# def update_task(id:int):
#     task = task_schema.load(request.json)
#     response_builder = ResponseBuilder()
#     data =  task_schema.dump(task_service.update(task, id))
#     if data:
#         response_builder.add_message("Task updated").add_status_code(100).add_data(data)
#         return response_schema.dump(response_builder.build()), 200
#     else:
#         response_builder.add_message("Task NOT updated - Project ID not found").add_status_code(404).add_data({'id': id})
#         return response_schema.dump(response_builder.build()), 404

# # Get: JSON con los datos de la task buscado por nombre de task
# @task.route('/tasks/name/<name>', methods=['GET'])
# def find_by_name(name:str):
#     response_builder = ResponseBuilder()
#     data = task_schema.dump(task_service.find_by_name(name))
#     if data:
#         response_builder.add_message("Task found").add_status_code(200).add_data(data)
#         return response_schema.dump(response_builder.build()), 200
#     else:
#         response_builder.add_message("Task NOT found").add_status_code(404).add_data({'Name': name})
#         return response_schema.dump(response_builder.build()), 404

# # Post: Asigna una task a un usuario
# @task.route('/tasks/user/<int:user_id>/task/<int:task_id>', methods=['POST'])
# def add_user(user_id: int, task_id: int):
#     response_builder = ResponseBuilder()
#     data = task_schema.dump(task_service.add_user(task_id, user_id))
#     if data:
#         response_builder.add_message("User added").add_status_code(200).add_data(data)
#         return response_schema.dump(response_builder.build()), 200
#     else:
#         response_builder.add_message("User already added").add_status_code(404).add_data({'User ID': user_id, 'Task ID': task_id})
#         return response_schema.dump(response_builder.build()), 404
    
# # Post: Elimina la asignación de un usuario a una task
# @task.route('/tasks/user/<int:user_id>/task/<int:task_id>', methods=['PUT'])
# def delete_user(user_id: int, task_id: int):
#     response_builder = ResponseBuilder()
#     data = task_schema.dump(task_service.delete_user(task_id, user_id))
#     if data:
#         response_builder.add_message("User deleted").add_status_code(200).add_data(data)
#         return response_schema.dump(response_builder.build()), 200
#     else:
#         response_builder.add_message("User is not assigned to this task").add_status_code(404).add_data({'User ID': user_id, 'Task ID': task_id})
#         return response_schema.dump(response_builder.build()), 404

# # Get: JSON con los datos de los usuarios asignados a una task
# @task.route('/tasks/<int:task_id>/users', methods=['GET'])
# def get_users(task_id: int):
#     response_builder = ResponseBuilder()
#     data = user_schema.dump(task_service.get_users(task_id), many=True)
#     if data:
#         response_builder.add_message("Users found").add_status_code(200).add_data(data)
#         return response_schema.dump(response_builder.build()), 200
#     else:
#         response_builder.add_message("Users NOT found").add_status_code(404).add_data({'Task ID': task_id})
#         return response_schema.dump(response_builder.build()), 404