
from task_control.shared.infrastructure.persistence.base import Base

from task_control.shared.infrastructure.persistence.database import engine

from task_control.modules.tasks.infrastructure.persistence.models import TaskModel

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

if __name__=="__main__":
    init_db()
    print("shéma sql initialisé")




