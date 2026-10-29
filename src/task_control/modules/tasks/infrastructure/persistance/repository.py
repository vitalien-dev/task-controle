
from sqlalchemy.orm import Session

from task_control.modules.tasks.domain.entities import Task ,Priority
from task_control.modules.tasks.application.use_cases.create_task import CreateTask  
from task_control.modules.tasks.application.ports.task_repository import TaskRepository
from task_control.modules.tasks.infrastructure.persistance.models import TaskModel


class SqlAlchemyTaskRepository:
    """ l'adaptateur de persistance qui utilise Sqlachemey """

    def __init__(self,session:Session):
        self._session=session

    def save(self,task:Task):
        record=TaskModel(
            title=task.title,
            description=task.description,
            priority=task.priority.value,
            status=task.status.value
        )

        self._session.add(record) # indique à sqlachemy que l'object doit etre persisté; l'insertion sql n'est pas executé immediatement 
        self._session.flush() # envoie l'operation en attente dans labse
        # self._session.commit() # pas de commit ici parceque save() ne decide pas seul du moment ou la transaction complete est validée

        task.id=record.id # on attribue l'id à l'entite metier pour que le usecase puisse le renvoyer à son appelant 

        return task
