
from task_control.modules.tasks.application.ports.task_repository import TaskRepository

from task_control.modules.tasks.domain.entities import Task,Priority


class CreateTask:
    """ Case d'utilisation : Créer un tache"""

    def __init__(self,task_repository:TaskRepository) -> None:
        self._task_repository=task_repository

    def execute(
        self,
        title:str,
        description:str="",
        priority:Priority=Priority.MEDIUM
    ) -> Task:

        # instanciation pour la creation de la task
        task = Task(title,description,priority)

        # on sauvegarde maintenant la task
        return self._task_repository.save(task)

      

