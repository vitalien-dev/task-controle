from task_control.shared.infrastructure.persistence.base import Base
from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy import String , DateTime



class UserModel(Base):

    __tablename__ = "users"

    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    email:Mapped[str]=mapped_column(String(320),unique=True,nullable=False)
    hashed_password:Mapped[str]=mapped_column(String(255),nullable=False)

    