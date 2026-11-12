

from collections.abc import Generator
from sqlalchemy.orm import Session
from task_control.shared.infrastructure.persistence.database import SessionLocal 

from typing import Annotated
from fastapi import Depends

from task_control.modules.tasks.application.ports.unite_of_work import TaskUnitOffWork
from task_control.modules.tasks.application.use_cases.create_task import CreateTask
from task_control.modules.tasks.infrastructure.persistence.unite_of_work import SqlAlchemyTaskUnitOfWork  

from task_control.modules.identity.application.ports.unit_of_work import IdentityUnitOfWork
from task_control.modules.identity.application.ports.password_hasher import PasswordHasher
from task_control.modules.identity.application.use_cases.create_user import CreateUser

from task_control.modules.identity.infrastructure.persistance.unit_of_work import SqlAlchemyIdentityUnitOfwork 
from task_control.modules.identity.infrastructure.security.bcrypt_pasword_hasher import  BcryptPasswordHasher

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



def get_identity_uow(session:SessionDep) -> IdentityUnitOfWork:
    return SqlAlchemyIdentityUnitOfwork(session)


def get_password_hasher() -> PasswordHasher:
    return  BcryptPasswordHasher(rounds=12)


def get_create_user(
        uow: Annotated[
            IdentityUnitOfWork,
            Depends(get_identity_uow)
        ],

        password_hasher: Annotated[
            PasswordHasher,
            Depends(get_password_hasher)
        ]
) -> CreateUser:

    return CreateUser(
        uow=uow,
        password_hasher=password_hasher
    )

