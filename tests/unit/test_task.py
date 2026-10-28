
import pytest

from task_control.modules.tasks.domain.entities import Task,Priority,TaskStatus

def test_task_uses_default_priority_and_status():

    task=Task("Become devops/cloud ingenier")

    assert task.priority==Priority.MEDIUM
    assert task.status==TaskStatus.TODO


def test_task_stripe_title():

    task=Task("Learn clean architecture")
    assert task.title=="Learn clean architecture"

def test_task_reject_empty_title():
    with pytest.raises(ValueError):
        Task(title="")

def test_task_reject_title_longer_than_120():
    with pytest.raises(ValueError):
        Task("A"*121)

def test_mark_done_changes_status():
    task=Task("Ecrivons les tests")

    task.mark_done()
    assert task.status==TaskStatus.DONE

# ----------- rename task --------------
def test_task_rename_stripe_title():
    task_rename= Task("Title on th task. ")
    task_rename.renam("  I rename this task  ")
    assert task_rename.title=="I rename this task"

def test_task_empty_title():
    task_rename=Task("Bienvenue a maori")
    with pytest.raises(ValueError):
        task_rename.renam(" ")

def test_task_rename_len_120():
    task_rename= Task("I rename this task. ")
    with pytest.raises(ValueError):
        task_rename.renam("A"*121)

def test_task_valide_rename():
    task_rename=Task("Titre principale entré")
    task_rename.renam("Titre renommé") 
    assert task_rename.title == "Titre renommé" 
    


