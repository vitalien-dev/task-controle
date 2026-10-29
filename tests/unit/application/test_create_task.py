import pytest
from task_control.modules.tasks.application.use_cases.create_task import CreateTask
from task_control.modules.tasks.domain.entities import Task,Priority,TaskStatus


class InMemoryTaskRepository:
    """ Faux depot utilisé uniquement pour les tests"""

    def __init__(self)-> None:
        self.saved_tasks:list[Task]=[]

    def save(self,task:Task)-> None:
        self.saved_tasks.append(task)


def test_create_task_save_task():
    repository= InMemoryTaskRepository()
    use_case=CreateTask(repository)

    task = use_case.execute(title="preparer la pipe line Ci",description="gerer le workflow de test",priority=Priority.HIGH)

    assert task.title == "preparer la pipe line Ci"
    assert task.priority == Priority.HIGH
    assert task.status == TaskStatus.TODO

    assert len(repository.saved_tasks) == 1
    assert repository.saved_tasks[0] == task


def test_create_task_reject_empty_title_without_saving():
    repository= InMemoryTaskRepository()
    use_case=CreateTask(repository)

    with pytest.raises(ValueError):
        use_case.execute(title="   ")

    assert repository.saved_tasks == []

#-----------------

def test_create_task_accepts_high_priority():
    repository=InMemoryTaskRepository()
    use_case=CreateTask(repository)

    task=use_case.execute(title="First title",description="cette description est la pour nous",priority=Priority.HIGH)

    assert task.priority == Priority.HIGH
    assert task.description == "cette description est la pour nous"
    assert isinstance(task,Task)

    assert len(repository.saved_tasks) == 1
    assert repository.saved_tasks[0] is task



