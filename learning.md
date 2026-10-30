# partie 1

## Exercices 2: Vérificatioin de la comprehension

* **Question A :** Quelle est la différence entre un schéma Pydantic qui reçoit les données d'un endpoint et l'entité métier Task ?

    - la difference reside dans le fait que l'entité metier est indepandant de toute ressources externe.

        `Resultat ia: Pydantic valide et structure les données à la frontière de l'application, tandis que l'entité métier représente le concept Task et porte ses règles métier.  `

* **Question B :** Pourquoi avons-nous choisi de mettre la règle ``« un titre ne peut pas être vide »`` dans le domaine plutôt que uniquement dans une route FastAPI ?

    - car ceci fait partie de la logique metier que nous voulons de notre app, indepandament de toute techno.

* **Question C :** Une dataclass déclare ``priority: Priority``. Pourquoi avons-nous quand même écrit une vérification ``isinstance(self.priority, Priority) ?``

    - pour s'assurer en avance du type de la valeur et le catcher en avance
        `une annotation comme priority: Priority ne garantit pas à elle seule que la valeur sera une instance de Priority à l'exécution. Une dataclass ne réalise pas automatiquement cette validation.  `

* **Question D. :** Si nous changeons demain ``SQLAlchemy`` pour un autre mécanisme de stockage, quelles parties de cette leçon devraient rester utilisables sans modification ? Explique pourquoi.

    - le domaine , donc entities parcequ'elle est ecrite en python pur et n'est depandante d'aucune techno externe


# partie 2

## EXercice B: Raisonnement architecturale

1. Pourquoi avons-nous créé TaskRepository au lieu d'importer directement SQLAlchemy dans CreateTask ?
    
    - pour appliquer le principe d'injection de depandance et empche toute depandance d'un usecase a une tehno.

    `
        La nuance importante est que le port représente l'abstraction, tandis que l'injection de dépendances consiste à fournir l'implémentation nécessaire au cas d'utilisation. Le principe de conception auquel cela contribue est l'inversion des dépendances.
    `
2. Si nous remplaçons ``InMemoryTaskRepository`` par ``SqlAlchemyTaskRepository``, quelle partie du code devrait rester inchangée ? Pourquoi ?
    
    - le use case doit rester inchangé ainsi que le port

3. Si je décide de mettre toute la logique de création dans la route ``FastAPI``, puis d'appeler directement ``session.add()`` ``et session.commit()``, quel problème architectural risquons-nous de recréer ?
    
    - on va creer une depandance vis a vis de fastapi

        `
            Tu as identifié une dépendance envers FastAPI, mais il y a un deuxième problème tout aussi important : la route serait également couplée à SQLAlchemy et à la persistance.

            La couche de présentation gérerait alors à la fois HTTP, l'orchestration de la création et les opérations de base de données. Cela rendrait le code plus difficile à tester isolément, à réutiliser et à faire évoluer.
        `


## EXercice C: verification pratique

1. lancement du test et rendu



# partie 3

## EXercice B: Reponse avec mes mots propres

1. Quelle est la différence entre Task et TaskModel ? Pourquoi avons-nous choisi de conserver les deux ?

    - la difference entre ``Task`` et ``TaskModel`` est que Task est notre model metier de notre entité alors que TaskModel est la classe qui creer notre table en BD en s'inspirant de Task , avec l'orm choisir, c'est à dire sqlalchemy dans notre cas

2. Que se passe-t-il lorsque nous appelons ``session.add(record)`` ? Et pourquoi avons-nous ensuite appelé ``session.flush()`` ? 

    - lorsque nous faisons ``session.add(record)`` on prepare les donné qui vont etre persité et par la suite quant on fait ``session.flus()``... jai pas bien compris cette ligne

    ### correction
        | Instruction |	Fonction |
        | session.add() |	Ajoute l'objet à l'unité de travail de la session |
        | session.flush() |	Envoie les opérations SQL en attente à la base, sans valider la transaction | 
        | session.commit() |	Effectue le flush nécessaire puis valide la transaction |
        | session.rollback() |	Annule les opérations de la transaction non validée |
        

3. Quelle est la différence entre flush() et commit() ?

    - la difference entre un ``flush()`` et un ``commit()`` est que le commit push directement les données en DB

    ### Corection 
        | La distinction entre flush et commit est particulièrement importante : une opération envoyée à la base par flush() peut encore être annulée par un rollback(). |

4. Pourquoi avons-nous utilisé ``with TestSession.begin() as session`` dans le test ?

    - pour s'assurer de la fermeture de la session après les operation; au cas ou engine.dispose() viendrai à avoir un probleme

    ### Correction

    1. Il crée une nouvelle session.
    2. Il ouvre une transaction.
    3. À la sortie du bloc, il valide la transaction si tout s'est bien passé, l'annule en cas d'exception et ferme la session.

        C'est donc une manière pratique de gérer automatiquement le cycle de vie de la session et de la transaction.

        Une nuance importante : engine.dispose() n'est pas responsable de la fermeture de cette session. Il concerne la gestion du pool de connexions du moteur SQLAlchemy.



# partie 4

## EXercice A: Premiere migration

1. Installer Alembic.
    
    - pour installer alembic on tape ``uv run add alembic`` on ajoute pas de ``--dev`` car c'est une depandance necessaire pour le maintien et l'volution de notre app en prod


2. Initialiser l'environnement de migration.

    - pour initialiser l'environnement de migration on tape la commande ``uv run alembic init alembic``


3. Configurer env.py.

    - pour a configuration de env.py on aura besoin de l'url de la db de notre ``Base `` pour exploiter les metadata de l'app , du dossier ``model`` qui contient tous les model de notre app, qui va fournir de maniere implicite les model l'attribut metadata  


4. Générer la migration de la table tasks.

    - pour generer les migrations de la table tasks on tape ``uv run alembic revision --autogenerate -m "gen migration"``


5. Examiner le fichier généré.

    - on observe l'id de la migration avec les fonctions ``upgrade()`` pour les operation effectuer et ``downgrade()`` pour le retour en arriere


5. Appliquer la migration.

    - pour appliquer les migration on tape la  commande ``uv run alembic revision upgrade head``

6. Vérifier la révision actuelle.
    - pour verifier la migration actuelle on tape le commande ``uv run alembic current``
