from datetime import datetime

def calculer_annee_100_ans():
    try:
        # Demander l'âge de l'utilisateur
        âge = int(input("Veuillez entrer votre âge : "))

        # Obtenir l'année actuelle
        année_actuelle = datetime.now().year

        # Calculer l'année où l'utilisateur aura 100 ans
        année_100_ans = année_actuelle + (100 - âge)

        # Afficher le résultat
        print(f"Vous aurez 100 ans en l'an {année_100_ans}.")

    except ValueError:
        print("Veuillez entrer un âge valide (nombre entier).")

# Appeler la fonction
calculer_annee_100_ans()
