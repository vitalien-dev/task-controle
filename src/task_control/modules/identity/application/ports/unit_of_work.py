from typing import Protocol
from task_control.modules.identity.application.ports.user_repository import UserRepository


class IdentityUnitOfWork(Protocol):

    users: UserRepository
    
    def commit(self) -> None:
        ...

    def rollback(self)  -> None:
        ...





