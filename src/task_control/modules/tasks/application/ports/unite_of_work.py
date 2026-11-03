from typing import Protocol

from task_control.modules.tasks.application.ports.task_repository import TaskRepository


class TaskUnitOffWork(Protocol):

    task = TaskRepository # on depose les taches accessible pendant le travil
    def commit(self)  -> None :

        ...

    def rollback(self)  -> None:
        ...








