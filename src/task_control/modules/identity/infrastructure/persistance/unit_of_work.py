from sqlalchemy.orm import Session
from task_control.modules.identity.infrastructure.persistance.repository import SqlAlchemyUserRepository

class SqlAlchemyIdentityUnitOfwork:

    def __init__(self,session:Session):

        self._session = session
        self.users = SqlAlchemyUserRepository(self._session)

    def commit(self) -> None: 
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
        
         