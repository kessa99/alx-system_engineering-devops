Play with AP


#### STEP FOR USE API REST ###

#!/usr/bin/python3
"""Script python with API Rest to import information"""

"""
Importations des elements dont on aura besoin pour le script
*json pour retourner des formats serialiser ou deserialiser*
*requests pour les requettes HTTP*
*sys pour utiliser les qrguments*
"""
import json
import requests
import sys

if __name__ == "__main__":
"""
1- verifier que le bon nombre dùqrgument a bien été passé en paramètre: if len(sys.argv) > 1:

2-passer les elments du paramètre dans une variable: user = sys.argv[1]

3- mettre l'api dans une variable. C'est de  là que nous allons pouvoir tirer, extraire les données pour les afficher ou les manier comme l'on veut: url = "https://jsonplaceholder.typicode.com/"

4- Il est temps d'envoyer une requête HTTP GET pour avoir les données à afficher grace à :

rpse = requests.get("{}users/{}".format(url, user))
de façons générale on aura un truc comme ça: https://jsonplaceholder.typicode.com/users/sys.argv[1]

où le sys.argv represente l'objet n de la liste Json

5- Maintenant une fois toute la liste obtenu, je la transforme en format JSON ou je pour utiliser des spécifications pour tirer certains éléménts via get et notera l'entête avec le "name" pour tirer les noms."

        name = rpse.json().get("name")

6- Affichons les conditions. Si le nom existe alors nous allons recuperer la to do list caractérisé par todo qui est un entête de l'userId donné en fonction du user saisie bien sûr il sera mis dans une variable

        if name is not None:
            scd_rpse =
            requests.get("{}todo?userId={}".format(url, user)).json()

7- Etant donné que la donnée extraite de la todo list est donné dans la variable scd_rpse on peut donc connaitre sa longueur
            all_task = len(scd_rpse)

8- Il faut maintenant savoir combien ont été faite. Pour se faire nous avons normalement les sections des objet qui parle de taches complète faite ou non. 
            done_task = []

            for task in scd_rpse:
                if task.get("completed") is True:
                    done_task.append(task)
            count = len(done_task)

9- Afficher la solution comme demandé
            print("Employee {} is done with tasks({}/{}): ".format(name, count, done_task))

10- Afficher les tache faite
            for title in done_task:
                print("\t {}".format(title.get("title")))
