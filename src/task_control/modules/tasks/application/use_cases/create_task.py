
from task_control.modules.tasks.application.ports.task_repository import TaskRepository

from task_control.modules.tasks.domain.entities import Task,Priority

from task_control.modules.tasks.application.ports.unite_of_work import TaskUnitOffWork  


class CreateTask:

    """ Case d'utilisation : Créer un tache"""

    def __init__(self,uow:TaskUnitOffWork) -> None:
        self._uow=uow


    def execute(
        self,
        title:str,
        description:str="",
        priority:Priority=Priority.MEDIUM
    ) -> Task:

        # instanciation pour la creation de la task
        task = Task(
            title=title,
            description=description,
            priority=priority
            )

        try:
            saved_task=self._uow.task.save(task=task)

            self._uow.commit()

            return saved_task

        except Exception:
            self._uow.rollback()

            raise

        

      

