from dataclasses import dataclass


@dataclass
class User:
    email:str
    hashed_password:str
    id:int | None = None

    def __post_init__(self) -> None:

        if not isinstance(self.email,str):
            raise TypeError("L'email doit etre une chaine de caractere")

        self.email=self.email.strip().lower()

        if not self.email :
            raise ValueError("L'email est obligatoire")


        if not isinstance(self.hashed_password,str):
            raise TypeError("Le mot de passe est invalide")

        if not self.hashed_password:
            raise ValueError("le mot de passe est obligatoire ")

        