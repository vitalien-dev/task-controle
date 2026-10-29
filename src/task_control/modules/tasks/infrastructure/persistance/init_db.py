
from task_control.modules.tasks.infrastructure.persistance.base import Base 
from task_control.modules.tasks.infrastructure.persistance.database import engine

from task_control.modules.tasks.infrastructure.persistance.models import TaskModel

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

if __name__=="__main__":
    init_db()
    print("shéma sql initialisé")




