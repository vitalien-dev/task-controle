
from typing import Protocol


class PasswordHasher(Protocol):

    def hash(self,password:str)  -> None:
        """ Transforme le mot de passe en empreinte """
        ...

    def verify(self,password:str,hashed_password:str)  -> bool:
        """ Verify l'identité du mot de passe """
        ...



