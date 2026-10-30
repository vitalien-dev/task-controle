

from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine

from task_control.modules.tasks.application.use_cases.create_task import CreateTask
from task_control.modules.tasks.application.ports.task_repository import TaskRepository

from task_control.modules.tasks.domain.entities import Priority , Task ,TaskStatus
from task_control.modules.tasks.infrastructure.persistance.models import  TaskModel
from task_control.modules.tasks.infrastructure.persistance.base import  Base
from task_control.modules.tasks.infrastructure.persistance.repository import SqlAlchemyTaskRepository


def test_create_task_is_persisted_in_sqlite(tmp_path):

    data_base_file = tmp_path / "task_controle.db"

    engine = create_engine(f"sqlite:///{data_base_file}")
    Base.metadata.create_all(engine)


    TestSession = sessionmaker(
        engine,
        expire_on_commit=False
    )

    try:

        with TestSession.begin() as session:
            repository=SqlAlchemyTaskRepository(session=session)
            use_case= CreateTask(repository)

            task=use_case.execute(
                title="Créer la pipeline CI",
                description="Exécuter les tests automatiquement",
                priority=Priority.HIGH,
            )

            assert isinstance(task,Task)
            assert task.id is not None

            task_id = task.id


        # Le bloc transactionnel précédent est terminé :
        # nous ouvrons une nouvelle session pour vérifier la persistance.
        with TestSession() as session:
            saved_record = session.get(TaskModel, task_id)

            assert saved_record is not None
            assert saved_record.title == "Créer la pipeline CI"
            assert saved_record.description == (
                "Exécuter les tests automatiquement"
            )
            assert saved_record.priority == "high"
            assert saved_record.status == "todo" 

    finally:
        engine.dispose()

        
def test_task_saved_with_priority_low(tmp_path):

    tas_db= tmp_path/"task_controle.db"
    DATABASE_URL=f"sqlite:///{tas_db}"

    engine=create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    TestSession=sessionmaker(engine,expire_on_commit=False)

    try:
        with TestSession.begin() as session:
            repository=SqlAlchemyTaskRepository(session)
            use_case=CreateTask(repository)

            task=use_case.execute(
                title="Titre du test num 2",
                description="Description du test num 2",
                priority=Priority.LOW,
                
            )

            task_id=task.id

            assert task.priority.value == "low"
            assert task.status.value == "todo"
            assert task.id is not None

        # on verifie la persistance des donnée
        with TestSession() as session:  # nous utilisons ici le TestSession() sans le begin parceque nous voulons seulement lire les data deja saved
            saved_task=session.get(TaskModel, task_id)

            assert saved_task.id is not None
            assert saved_task.title == "Titre du test num 2"
            assert saved_task.description == "Description du test num 2"
            assert saved_task.priority == "low"
            assert saved_task.status == "todo"

    finally:
        engine.dispose()




