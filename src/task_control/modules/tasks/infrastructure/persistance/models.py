from sqlalchemy import String,Text,DateTime
from sqlalchemy.orm import mapped_column,Mapped
from datetime import datetime

from task_control.modules.tasks.infrastructure.persistance.base import Base


class TaskModel(Base):

    __tablename__ = "task"

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str] =mapped_column(String(120),nullable=False)
    description:Mapped[str] = mapped_column(Text,nullable=False,default="")

    priority:Mapped[str]=mapped_column(String(20),nullable=False)
    status:Mapped[str]=mapped_column(String(100),nullable=False)

    # pour gerer l'echéance de la task
    due_date:Mapped[datetime] = mapped_column(DateTime(),nullable=True)
    
    
