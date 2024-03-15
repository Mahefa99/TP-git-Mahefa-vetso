import json

def main():

    choix = input("Que souhaitez-vous faire ? (charger/créer) ")

   if choix == "charger":
        charger_liste_taches()

    elif choix == "créer":
        creer_liste_taches()


    else:
        print("Choix invalide !")


def charger_liste_taches():

    with open("liste_taches.json", "r") as fichier:
        liste_taches = json.load(fichier)


    for i, tache in enumerate(liste_taches):
        print(f"{i+1} - {tache}")


def creer_liste_taches():
    liste_taches = []


    nom_tache = input("Entrez le nom de la tâche : ")


    liste_taches.append(nom_tache)


    sauvegarder_liste_taches(liste_taches)


def sauvegarder_liste_taches(liste_taches):

    sauvegarder = input("Souhaitez-vous sauvegarder la liste de tâches ? (oui/non) ")

    if sauvegarder == "oui":
        with open("liste_taches.json", "w") as fichier:
            json.dump(liste_taches, fichier)

if __name__ == "__main__":
    main()
