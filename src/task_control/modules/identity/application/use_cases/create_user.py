from task_control.modules.identity.application.ports.unit_of_work import IdentityUnitOfWork
from task_control.modules.identity.application.ports.password_hasher import PasswordHasher 
from task_control.modules.identity.domain.entities import User


class CreateUser:

    def __init__(self,uow:IdentityUnitOfWork,password_hasher:PasswordHasher):

        self._uow=uow
        self._password_hasher = password_hasher

    def execute(self,email:str,password:str) -> User:

        normalized_email=email.strip().lower()

        existing_user = self._uow.users.get_by_email(normalized_email)

        if existing_user is not None:
             raise ValueError("cet email existe deja !")

        hashed_password = self._password_hasher.hash(password=password)

        user = User(
            email=email,
            hashed_password=hashed_password
        )

        try:

            saved_user=self._uow.users.save(user)
            self._uow.commit()

            return saved_user

        except:
            self._uow.rollback()
            raise
            

            

##
# Étudions les responsabilités dans l'ordre :
# 1. Normaliser l'adresse e-mail.
# 2. Vérifier si l'utilisateur existe déjà.
# 3. Demander au service de sécurité de hacher le mot de passe.
# 4. Construire l'entité métier User.
# 5. Sauvegarder l'utilisateur avec le Repository.
# 6. Valider la transaction avec le Unit of Work.
# 7. Renvoyer l'utilisateur.



