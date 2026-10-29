
from typing import Protocol
from task_control.modules.tasks.domain.entities import Task

class TaskRepository(Protocol):
    """
        cette classe represente le contrat de persistance des taches
        1.Protocole definir le contrat sur les methodes qu'un objet doit posseder.
    """

    # cette methode signifie que notre objet donc l'instance de cette classe aura besoin d'un objet 
    # capable de recevoir une tache et de la sauvegarder.
    def save(self,task:Task)  ->  Task:
        """ sauvagarde des taches et Retourne une tache persitée"""
        ... # ceci veut dire corp volontairement absent pour pemertre a qui veut satifaire le contrat d'utiliser a sa guise ces outils
