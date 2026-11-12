from typing import Protocol
from task_control.modules.identity.domain.entities import User

class UserRepository(Protocol):

    def get_by_email(self,email:str)  -> User | None:
        ... 

    def save(self,user:User)  -> User :
        ...

     