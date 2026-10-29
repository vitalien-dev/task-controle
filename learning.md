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


