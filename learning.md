
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

