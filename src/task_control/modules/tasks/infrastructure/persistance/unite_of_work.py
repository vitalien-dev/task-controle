
from sqlalchemy.orm import Session

from task_control.modules.tasks.infrastructure.persistance.repository import SqlAlchemyTaskRepository


class SqlAlchemyTaskUnitOfWork:

    def __init__(self,session:Session):
        self._session=session

        self.task=SqlAlchemyTaskRepository(session) # on cree un depot en utilisant la session recu

    def commit(self) -> None:
        self._session.commit() # on delegue la validation de la transaction à sqlAlchemy

    def rollback(self) -> None:
        self._session.commit()

        

    



