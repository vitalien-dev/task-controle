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
    
    - pour installer alembic on tape ``uv  add alembic`` on ajoute pas de ``--dev`` car c'est une depandance necessaire pour le maintien et l'volution de notre app en prod


2. Initialiser l'environnement de migration.

    - pour initialiser l'environnement de migration on tape la commande ``uv run alembic init alembic``


3. Configurer env.py.

    - pour a configuration de env.py on aura besoin de l'url de la db de notre ``Base`` pour exploiter les metadata de l'app , du dossier ``model`` qui contient tous les model de notre app, qui va fournir de maniere implicite les model l'attribut metadata  


4. Générer la migration de la table tasks.

    - pour generer les migrations de la table tasks on tape ``uv run alembic revision --autogenerate -m "gen migration"``


5. Examiner le fichier généré.

    - on observe l'id de la migration avec les fonctions ``upgrade()`` pour les operation effectuer et ``downgrade()`` pour le retour en arriere


5. Appliquer la migration.

    - pour appliquer les migration on tape la  commande ``uv run alembic upgrade head``

6. Vérifier la révision actuelle.
    - pour verifier la migration actuelle on tape le commande ``uv run alembic current``



# partie 5

## EXercice A: Analyse de code

1. Je veux que tu distingues clairement le rôle de ``SessionLocal`` et celui de ``session``.

    - ``SessionLocal`` est la classe qui fabrique une ``session``, ainsi session est une instance de SessionLocal qui va etre passé a chaque requette vers le serveur 


## Exercice B: Comprendre yield

1. Pourquoi utilisons nous ``yield`` plutot que ``return``

    - ``yield`` est preféré à ``return`` parcequ'il ne renvoie qu'une seule fois une connection database à l'appel

2. Quand le bloc ``finally`` sera-t-il exécuté ?

    - finally sera toujours executer a chaque passe au try , pour liberer la ressource 

3. Que se passe-t-il si une exception est déclenchée pendant l'exécution de la route ?

    - si une exception est declanché elle sera passé sous silence car il y'a pas de raise pour faire remonter l'erreur 


## Exercice C — Injection de dépendances

1. Pourquoi la deuxième approche est-elle préférable dans notre architecture ? Identifie au moins trois avantages.

    - la deuxieme approche est preferable parceque:

        * elle ne depand pas de sqlachemy
        * l'injection de depandance permet egalement de s'extraire de cette depandace vis à vis des technologie
        * en consequence on aura une maintenance facile  


## Exercice D — Diagnostic d'une erreur

1. après une erreur SQLAlchemy pendant un flush().
    Quelles conséquences cela peut-il avoir si nous essayons de réutiliser la même session ?

    * la transaction etant consus suivant un pricipe d'atomicité, toute les operation precedante seront annulé
        et si l'on utilise la meme session elle ne sera plus valide parceque elle aura deja été revoqué du fait de l'erreur. donc ceci voudrai dire que chaque requette à sa propre session creeé? je veut comprendre 

    



# partie 6:  évaluation pédagogique
Nous avons maintenant abordé plusieurs nouveaux concepts. Je veux vérifier que tu ne te contentes pas de suivre les instructions, mais que tu comprends les décisions architecturales et sécuritaires.


## Exercice A — Comprendre bcrypt
Explique avec tes propres mots :

1. Pourquoi stocker un mot de passe en clair est-il dangereux ?
    - en cas de pirate de la db les mdp pourrait etre recuperer et utilisé à de fin malsaine

2. Pourquoi deux utilisateurs ayant exactement le même mot de passe peuvent-ils avoir deux hash différents ?
    - ils pourrait avoir deux hash different car un ``sel`` different est generé par bcryp à chaque operation et ajouter au hash 

3. Pourquoi ne pouvons-nous pas simplement comparer le hash nouvellement généré avec celui enregistré ?
    - parcequ'il sera automatiquement different de ce qui est stoké du fait du ``sel``

4. Quelle est la différence entre hash() et verify() ?
    - hash a pour role de hasher le mdp tandisque verify va plutot comparer l'exactitude


## Exercice B — Architecture hexagonale

1. Pourquoi avons-nous créé un port PasswordHasher au lieu d'importer directement bcrypt dans CreateUser ?
    - pour eviter de depandre de bcrypt

Imagine que nous décidions demain de remplacer bcrypt par Argon2id.

2. Quels éléments de notre architecture devraient changer ? Lesquels devraient rester identiques ?
    - l'element qui devrai changer est l'adaptateur ``bcrypt_passwor_hash`` et ce ui devrai rester est le port ou encore la facade password_hasher


## Exercice C — Sécurité des données
Voici deux réponses possibles de notre API.

Réponse A :
{
  "id": 1,
  "email": "user@example.com",
  "hashed_password": "$2b$12$..."
}

Réponse B :
{
  "id": 1,
  "email": "user@example.com"
}

1. Pourquoi la réponse B est-elle préférable, même si le mot de passe est déjà haché ?
    - parceque le mdp peut toujours etres exploité s'il tombe entre les mauvaise main, autant ne pas l'envoyé   c'est toujours dangereux d'exposer le payload au client puiqu'il est uniquement signé


## Exercice D — Diagnostic d'un problème métier
Supposons que deux requêtes arrivent presque simultanément.

Elles essaient toutes les deux de créer un compte avec :
user@example.com

1. Les deux vérifications get_by_email() peuvent-elles renvoyer None avant que l'une des inscriptions soit enregistrée ?
    - oui 

2. Explique ensuite pourquoi unique=True dans UserModel reste indispensable.
    - pour garantir l'unicité au niveau de la db au cas ou sa echaperait à ``get_by_email()``

    
## Exercice E — Tests
Écris au moins trois tests supplémentaires :
- L'inscription d'un utilisateur doit enregistrer un hash et non son mot de passe original.
- Une adresse e-mail déjà enregistrée doit provoquer EmailAlreadyRegistered.
- Un mot de passe dépassant 72 octets doit être refusé.