from enum import Enum
from dataclasses import dataclass

class Priority(str,Enum):
    LOW="low"
    MEDIUM="medium"
    HIGH="high"

class TaskStatus(str,Enum):
    TODO="todo"
    IN_PROGRESS="in_progress"
    DONE="done"

@dataclass #pour eviter le code verbeux et de permetre à python  de gerer automatiquement __repr__ init__ etc..
class Task:
    title:str
    description:str=""
    priority:Priority=Priority.MEDIUM
    status:TaskStatus=TaskStatus.TODO
    id:int|None=None

    def __post_init__(self)->None:

        """ on applique les test sur le titre """
        if not isinstance(self.title,str):
            raise TypeError("le titre doit obligatoirement etre un chaine de caractere !")

        self.tilte=self.title.strip()

        if not self.title:
            raise ValueError(" Le titre est obligatoire.")

        if len(self.tilte) > 120:
            raise ValueError("Le tire ne doit pas depasser 120 caracteres") 


        """ on applique les test sur la description """
        if not isinstance(self.description,str):
            raise TypeError("la description doit obligatoirement etre un chaine de caractere !")

        self.tilte=self.description.strip()

        if len(self.description) > 2000:
            raise ValueError("La description ne doit pas depasser 2000 caracteres")


        """ on applique les test de l'enum """
        if not isinstance(self.priority,Priority):
            raise TypeError("LA proprieté est invalide")

        if not isinstance(self.status,TaskStatus):
            raise TypeError("Status invalide")

    #cette methode represente une operation que l'o peut effectuer sur une tache
    def mark_done(self)->None:
        self.status=TaskStatus.DONE


    def renam(self,new_title:str) -> None:
        """ Cette methode permet à l'user de modifier ses taches"""
        if not isinstance(new_title,str):
            raise TypeError("vous devez entrer uniquement les caracteres")

        new_title_striped=new_title.strip()

        if not new_title_striped:
            raise ValueError("le titre ne doit pas etre vide")
        

        
        if len(new_title_striped) > 120:
            raise ValueError("le texte ne doit pas depasser 120 caractere")
        
        
        self.title=new_title_striped

        


         