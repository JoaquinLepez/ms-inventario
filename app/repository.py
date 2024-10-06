from typing import List
from app import db
from app.models import Stock

class StockRepository:
    def all(self) -> List[Stock]:
        return db.session.query(Stock).all()
    
# class TaskRepository:

#     def save(self, task: Task) -> Task:
#         db.session.add(task)
#         db.session.commit()
#         return task
    
#     def update(self, task: Task, id: int) -> Optional[Task]:
#         entity = self.find(id)
#         if entity:
#             entity.name = task.name
#             entity.description = task.description
#             entity.start_date = task.start_date
#             entity.deadline = task.deadline
#             entity.priority = task.priority
#             entity.difficulty = task.difficulty
#             entity.state = task.state
#             db.session.add(entity)
#             db.session.commit()
#             return entity
#         else:
#             return None

#     def delete(self, id_task: id) -> None:
#         task = self.find(id_task)
#         db.session.delete(task)
#         db.session.commit()

#     def all(self) -> List[Task]:
#         tasks = db.session.query(Task).all()
#         return tasks
    
#     def find(self, id: int) -> Optional[Task]:
#         if id is None or id == 0:
#             return None
#         try:
#             return db.session.query(Task).filter(Task.id == id).one()
#         except:
#             return None
        
#     def find_by_name(self, name: str) -> Optional[Task]:
#         return db.session.query(Task).filter(Task.name == name).one_or_none()
    
#     def add_user(self, task: Task, user: User) -> Task:
#         if user in task.users:
#             return None
#         else:
#             task.users.append(user)
#             db.session.add(task)
#             db.session.commit()
#             return task
    
#     def delete_user(self, task: Task, user: User) -> Task:
#         if user in task.users:
#             task.users.remove(user)
#             db.session.add(task)
#             db.session.commit()
#             return task
#         else:
#             return None
    
#     def get_users(self, task: Task) -> List[User]:
#         return task.users
    