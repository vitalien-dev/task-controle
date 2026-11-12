from sqlalchemy import select
from sqlalchemy.orm import Session
from task_control.modules.identity.domain.entities import User
from task_control.modules.identity.infrastructure.persistance.models import UserModel

class SqlAlchemyUserRepository:

    def __init__(self,session:Session)  -> None :

        self._session=session

    def get_by_email(self,email:str) -> User | None:

        statement = select(UserModel).where(UserModel.email == email)

        record = self._session.scalar(statement)

        if record is None : 
            return None 

        return User(
            id=record.id,
            email=record.email,
            hashed_password = record.hashed_password
        )


    def save(self,user:User) -> None:

        record = UserModel(
            email=user.email,
            hashed_password = user.hashed_password
        )

        self._session.add(record)

        self._session.flush() # on fait le flush() pour recuperer l'id mais pas encore de commit

        # la decision transactionnel appartient à notre unité de travail (uow)

        user.id = record.id

        return user




        

