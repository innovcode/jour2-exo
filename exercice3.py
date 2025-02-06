def calculatrice():
    print("Bienvenue dans la calculatrice basique !")
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choix = int(input("Entrez le numéro de l'opération souhaitée (1/2/3/4) : "))

        if choix not in [1, 2, 3, 4]:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 4.")
            return

        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le second nombre : "))

        if choix == 1:
            resultat = nombre1 + nombre2
            print(f"Le résultat de l'addition est : {resultat}")
        elif choix == 2:
            resultat = nombre1 - nombre2
            print(f"Le résultat de la soustraction est : {resultat}")
        elif choix == 3:
            resultat = nombre1 * nombre2
            print(f"Le résultat de la multiplication est : {resultat}")
        elif choix == 4:
            if nombre2 != 0:
                resultat = nombre1 / nombre2
                print(f"Le résultat de la division est : {resultat}")
            else:
                print("Erreur : Division par zéro.")

    except ValueError:
        print("Veuillez entrer des nombres valides.")

# Appeler la fonction calculatrice
calculatrice()
