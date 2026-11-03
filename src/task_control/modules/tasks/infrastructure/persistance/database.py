from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL= "sqlite:///task_controle_alembic.db"


connect_args=(
    {"check_same_thread":False} 
    if DATABASE_URL.startswith("sqlite")
    else {}
)

engine=create_engine(DATABASE_URL,connect_args=connect_args)

SessionLocal=sessionmaker(engine,expire_on_commit=False)


