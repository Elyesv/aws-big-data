#### Table `Movies`
Imaginons que nous avons une table `Movies` avec les colonnes suivantes :
- `movie_id` (clé de partition type `S` UUID)
- `title` (type `S`)
- `release_year` (clé de tri type `N`)
- `genre` (type `S`)
- `rating` (type `N`)
- `details` (type `M` pour les détails JSON contenant des sous-objets comme `director` `duration` etc   )

1    **Configurer Boto3 et accéder à la table `Movies`**
   - Écrivez le code pour configurer Boto3 et accéder à la table `Movies`   

2    **Créer la table `Movies` avec un GSI sur `genre`**
   - Écrivez le code pour créer la table `Movies` avec un GSI sur la colonne `genre`   

3    **Insérer un film dans la table `Movies`**
   - Écrivez le code pour insérer le film suivant dans la table `Movies` :
    - `movie_id`: "uuid-1"
    - `title`: "Inception"
    - `release_year`: 2010
    - `genre`: "Sci-Fi"
    - `rating`: 8   8
    - `details`: {"director": "Christopher Nolan" "duration": 148}

4    **Insérer plusieurs films en utilisant `batch_writer`**
   - Écrivez le code pour insérer les films suivants en utilisant `batch_writer` :
    - `movie_id`: "uuid-2" `title`: "The Matrix" `release_year`: 1999 `genre`: "Action" `rating`: 8   7 `details`: {"director": "Wachowski" "duration": 136}
    - `movie_id`: "uuid-3" `title`: "Interstellar" `release_year`: 2014 `genre`: "Sci-Fi" `rating`: 8   6 `details`: {"director": "Christopher Nolan" "duration": 169}

5    **Récupérer un film par son `movie_id` et `release_year`**
   - Écrivez le code pour récupérer le film avec `movie_id` égal à "uuid-1" et `release_year` égal à 2010   

6    **Rechercher des films par `genre` en utilisant le GSI**
   - Écrivez le code pour rechercher tous les films du genre "Sci-Fi"   

7    **Rechercher des films sortis après 2000**
   - Écrivez le code pour rechercher tous les films sortis après l'année 2000   

8    **Rechercher des films avec une note supérieure à 8   5**
   - Écrivez le code pour rechercher tous les films avec une note supérieure à 8   5   

9    **Mettre à jour la note d'un film**
   - Écrivez le code pour mettre à jour la note du film "Inception" à 9   0   

10    **Supprimer un film de la table**
   - Écrivez le code pour supprimer le film avec `movie_id` égal à "uuid-2"   

11    **Ajouter un attribut JSON à un film**
   - Écrivez le code pour ajouter un attribut `awards` à "Inception" avec la valeur {"oscars": 4}   

12    **Rechercher des films avec une durée supérieure à 150 minutes**
   - Écrivez le code pour rechercher tous les films dont la durée est supérieure à 150 minutes   

13    **Compter le nombre total de films dans la table**
   - Écrivez le code pour compter le nombre total de films dans la table   

14    **Rechercher des films par genre et année de sortie en utilisant une clé composite**
   - Écrivez le code pour rechercher tous les films du genre "Sci-Fi" sortis après l'année 2000 en utilisant une clé composite   

15    **Rechercher des films dont le titre commence par 'I'**
   - Écrivez le code pour rechercher tous les films dont le titre commence par 'I'   

16    **Ajouter un GSI sur `release_year` et `rating`**
   - Écrivez le code pour ajouter un GSI sur les colonnes `release_year` et `rating`   

17    **Rechercher des films par `release_year` en utilisant le nouveau GSI**
   - Écrivez le code pour rechercher tous les films sortis en 2014 en utilisant le nouveau GSI   

18    **Rechercher des films avec une note supérieure à 8   5 en utilisant le nouveau GSI**
   - Écrivez le code pour rechercher tous les films avec une note supérieure à 8   5 en utilisant le nouveau GSI   

19    **Mettre à jour les détails d'un film**
   - Écrivez le code pour mettre à jour les détails du film "The Matrix" pour ajouter {"sequels": 2}   

20    **Supprimer tous les films d'un genre spécifique**
   - Écrivez le code pour supprimer tous les films du genre "Action"   

21    **Rechercher des films dont le réalisateur est "Christopher Nolan"**
   - Écrivez le code pour rechercher tous les films dont le réalisateur est "Christopher Nolan" en utilisant une expression d'attribut   

22    **Rechercher des films avec une durée comprise entre 120 et 180 minutes**
   - Écrivez le code pour rechercher tous les films dont la durée est comprise entre 120 et 180 minutes   

23    **Ajouter des critiques dans le sous-objet `details` d'un film**
   - Écrivez le code pour ajouter des critiques dans le sous-objet `details` du film "Inception" avec la valeur {"reviews": [{"reviewer": "John Doe" "comment": "Excellent!"} {"reviewer": "Jane Doe" "comment": "Amazing!"}]}   

24    **Rechercher des films dont une critique contient le mot "Amazing"**
   - Écrivez le code pour rechercher tous les films dont une critique contient le mot "Amazing"   

25    **Mettre à jour le champ `duration` d'un film en augmentant sa valeur de 10 minutes**
   - Écrivez le code pour mettre à jour le champ `duration` du film "Inception" en augmentant sa valeur de 10 minutes   

26    **Créer une table `Cinema` qui contient chacun les films et un nom**