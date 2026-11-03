

from collections.abc import Generator
from sqlalchemy.orm import Session
from task_control.modules.tasks.infrastructure.persistance.database import SessionLocal

from typing import Annotated
from fastapi import Depends

from task_control.modules.tasks.application.ports.unite_of_work import TaskUnitOffWork
from task_control.modules.tasks.application.use_cases.create_task import CreateTask
from task_control.modules.tasks.infrastructure.persistance.unite_of_work import SqlAlchemyTaskUnitOfWork  


def get_session()  -> Generator[Session,None,None]:

    session=SessionLocal()
    try:
        yield session

    except Exception:
        session.rollback()

        raise 
    finally:
        session.close()

SessionDep= Annotated[Session, Depends(get_session)] # on creer la session et on la fournir


def get_task_uow(session:SessionDep) -> TaskUnitOffWork: # on construit l'unité de travail avec la session

    return SqlAlchemyTaskUnitOfWork(session)


def get_create_task(uow:Annotated[Session,Depends(get_task_uow)]) -> CreateTask: # construit le cas d'utilisation

    return CreateTask(uow) # rzecois un createtask pret à etre creer 

