from .repository import StockRepository
from app.models import Stock

repository = StockRepository()

class StockService:

    def all(self) -> list[Stock]:
        return repository.all()
    
# class TaskService:

#     def save(self, task: Task) -> Task:
#         return repository.save(task)
    
#     def update(self, task: Task, id: int) -> Task:
#         return repository.update(task, id)
    
#     def delete(self, task_id: int) -> bool:
#         return repository.delete(task_id)
    
#     def all(self) -> List[Task]:
#         return repository.all()
    
#     def find(self, id: int) -> Task:
#         return repository.find(id)
    
#     def find_by_name(self, name: str) -> Task:
#         return repository.find_by_name(name)
    
#     def add_user(self, task_id: int, user_id: int) -> Task:
#         task = self.find(task_id)
#         user = user_service.find(user_id)
#         return repository.add_user(task, user)
    
#     def delete_user(self, task_id: int, user_id: int) -> Task:
#         task = self.find(task_id)
#         user = user_service.find(user_id)
#         return repository.delete_user(task, user)
    
#     def get_users(self, task_id: int) -> List[User]:
#         task = self.find(task_id)
#         return repository.get_users(task)