## Message pour Guy Amos
---

### Exercice 1

**Code original :**

```python
nom = "GUY"
ville ="yamoussoukro"
age = "20"
#afficher le nom,la ville et l age
print("je m appelle",nom,"\nj'ai",age,"et je vis à",ville)
```

**Commentaires :**

- **Bon travail** : Tu as bien déclaré les variables `nom`, `ville`, et `age`. C'est un bon début !
- **Typage des variables** : L'âge est une valeur numérique, il serait donc plus approprié de le déclarer comme un entier (`int`) plutôt qu'une chaîne de caractères (`str`). Cela permettrait de faire des calculs avec cette variable plus tard si nécessaire.
- **Faute de frappe** : Il y a une petite faute dans le message d'affichage : "je m appelle" devrait être "je m'appelle".
- **Correction proposée** :

```python
nom = "GUY"
ville = "yamoussoukro"
age = 20  # Correction : âge en tant qu'entier
# Afficher le nom, la ville et l'âge
print("Je m'appelle", nom, "\nJ'ai", age, "ans et je vis à", ville)
```

### Exercice 2

**Code original :**

```python
# entrer votre age
age = int(input("veiller saisir votre age  :"))
print("dans", 100 - age, "vous aurez 100 ans")
```

**Commentaires :**

- **Bonne logique** : Tu as bien compris comment demander une entrée utilisateur et effectuer un calcul simple.
- **Faute de frappe** : Il y a une faute dans le message : "veiller" devrait être "veuillez".
- **Clarté du message** : Le message final pourrait être plus clair pour l'utilisateur. Par exemple, préciser "ans" après le nombre d'années.
- **Correction proposée** :

```python
# Entrer votre âge
age = int(input("Veuillez saisir votre âge : "))
print("Dans", 100 - age, "ans, vous aurez 100 ans.")
```

### Exercice 3

**Code original :**

```python
# affichage du menu de la calculette
print("1.pour la somme")
print("2.pour la difference")
print("3.pour le produit")
print("4.pour la division")
# choix
choix = int(input("veiller effectuer un choix : "))
# veiller saisir un nombre
a = int(input("veiller saisir  un nombre1 : "))
b = int(input("veiller saisir un nombre2  : "))

# condition des operations
if choix == 1:
    print("la somme des nombres est : ", a + b)
elif choix == 2:
    print("la difference des nombres est : ", a - b)
elif choix == 3:
    print("le produit des nombres est : ", a * b)
else:
    print("la division des deux nombres est : ", a / b)
```

**Commentaires :**

- **Bon début** : Tu as bien structuré le menu et les choix pour la calculatrice.
- **Fautes de frappe** : Il y a des fautes dans les messages : "veiller" devrait être "veuillez".
- **Gestion des erreurs** : Il manque une vérification pour la division par zéro, ce qui peut provoquer une erreur si l'utilisateur entre `0` comme deuxième nombre.
- **Clarté des messages** : Les messages pourraient être plus clairs et uniformes.
- **Correction proposée** :

```python
# Affichage du menu de la calculatrice
print("1. Pour la somme")
print("2. Pour la différence")
print("3. Pour le produit")
print("4. Pour la division")

# Choix de l'opération
choix = int(input("Veuillez effectuer un choix : "))

# Saisie des nombres
a = int(input("Veuillez saisir un nombre 1 : "))
b = int(input("Veuillez saisir un nombre 2 : "))

# Condition des opérations
if choix == 1:
    print("La somme des nombres est :", a + b)
elif choix == 2:
    print("La différence des nombres est :", a - b)
elif choix == 3:
    print("Le produit des nombres est :", a * b)
elif choix == 4:
    if b != 0:
        print("La division des deux nombres est :", a / b)
    else:
        print("Erreur : Division par zéro.")
else:
    print("Choix invalide. Veuillez choisir une option entre 1 et 4.")
```

**Remarques générales :**

- **Clarté** : Assure-toi que tes messages sont clairs et sans fautes pour guider correctement l'utilisateur.
- **Gestion des erreurs** : Pense toujours aux cas où l'utilisateur pourrait entrer des données incorrectes ou inattendues.
- **Typage des variables** : Utilise le bon type de données pour les variables (par exemple, `int` pour les âges).

Continue comme ça, Guy ! Tu es sur la bonne voie pour maîtriser les bases de la programmation en Python.

## Mon conseil

Guy, continue sur cette voie en pratiquant régulièrement la programmation, même quelques minutes par jour. Travailler sur des projets personnels qui t'intéressent et lire le code d'autres développeurs t'aidera à progresser rapidement. N'hésite pas à utiliser les ressources en ligne pour poser des questions et apprendre de tes erreurs, car elles sont une partie normale du processus d'apprentissage. Avec de la persévérance, tu deviendras un excellent programmeur !