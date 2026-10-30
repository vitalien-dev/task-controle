from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL= "sqlite:///task_controle_alembic.db"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(engine,expire_on_commit=False)


