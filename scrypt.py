"""
Nommer une variable:            doit commencer par une lettre ou un underscore
                                ne pas contenir des caractères spéciaux
                                ne pas contenir d'espace

Type standards:                 entier numérique (int)
                                nombre flottant(float)
                                chaîne de caractères(str)
                                booléen(bool)
                                autres(listes, dictionnaires, tuples, etc.)

Fonction:                       print()                          -> afficher à l'écran
                                input()                          -> lire au clavier
                                type()                           -> retourne le type d'une donnée, variable, etc.
                                int(), float(), bool(), str()    -> "caster" une donnée, la convertir
                                formate()                        -> formater une chaine de caractères

Opérateurs en Python:           + (addition)
                                - (soustration)
                                * (multiplication)
                                / (division)
                                % (modulo) -> reste d'une division Euclidienne
                        
Opération de comparaison:       == (égale à)
                                != (différent de)
                                < (plus petit que)
                                > ( plus grand que)
                                <= (plus petit que ou égale à) 
                                >= (plus grand que ou égale à)
                                
Mots clés de condition:         if / elif / else
                                
Condition multiple:             and (ET)
                                or (OU)
                                in / not in (DANS / PAS DANS)
                                
Boucles:                        while / for

Mots-clés:                      break (casser la boucle) / continue (revenir au début de la boucle)


Modularité:                     Import <nom_module>
                                From <nom_module> import <nom_fonction>
                                From <nom_module> import *
                                
                                
Gestion des exceptions:               try / except (+ else, finally)

Type d'exceptions :             NameError -> Erreur de variable
                                ValueError -> Erreur de valeur
                                TypeError -> Erreur de type
                                ZeroDivisionError -> Erreur de division par zéro
                                OSError -> Erreur de système
                                AssertionError ->
                                
Méthode :                       Fonction sur une instance (objet)
Méthode de classe :             Fonction sur une classe
Méthode statique :              Fonction indépendante mais "liée" à une classe

"""





"""

# Création d'une fonction
# Les fonctions ont été mises en place afin d'éviter la répétition des méthodes au cas où le besoin se fait sentir.
# Une fonction est préfixée d'un mot clé def suivi du mot de la fonction. 
# Exemple: 
# def nom_de_la_fonction():
#     print("Je suis une fonction écrite en Python")
# nom_de_la_fonction()

# Fonction avec paramètre
# Les fonctions peuvent recevoir des paramètres
# Exemple :
# def nom_de_la_fonction(param):
#     print("Affiche moi le paramètre reçu ", param)
# nom_de_la_fonction("mon paramètre")

# Il est possible de définir des paramètres par défaut avant même de mettre la fonction en exécution 
# Exemple :

# def nom_de_la_fonction(param1 = "premier paramètre", param2 = "deuxième paramètre"):
#     print(param1, param2)
# nom_de_la_fonction("param1")

# Dans ce cas, le terminal va afficher: {param1 deuxième paramètre} // Parce que le deuxième paramètre est défini par défaut
# Mais si les deux paramètres sont définis, la fonction prendra en compte les deux paramètres renseignés lors de l'exécution


# Dans le cas où le nombre de paramètre n'est pas connu au préalable, on préfixe le paramètre par une étoile * 
# Exemple:

# def show_inventory(*args): # L'étoile permet de notifier que le paramètre à renseigner peut être plusieurs
#     for i in args:
#         print("\n", i)
        
# show_inventory("param1","param2","param3","param4","param5","param6","param7","param8","param9")




# Fonction lambda
# C'est une fonction qui n'a pas de nom et il est impossible d'appeler la fonction pour l'exécution:

lambda: print("Cette fonction ne peut pas être appelé car elle n'a pas de nom")

Pour l'utiliser, il faut l'assigner à une variable.
Exemple:

nom_variable = lambda: print("Cette fonction ne peut pas être appelé car elle n'a pas de nom")

nom_variable() // Ça affiche "Cette fonction ne peut pas être appelé car elle n'a pas de nom"


# Fonction lambda avec paramètre

taxe = lambda prix: prix + (prix * 20/100)
print(taxe(10)) // Ça affiche 12.0

Exemple: 

calculate = lambda a, b: a + b

print(calculate(2,5)) // Ça affiche 5

NB: lambda remplace le mot clé def
"""


# nom = "AZANKPO"
# prenom = "Erik"
# age = 20
# prix = 15.5
# condition = True

# print(type(int(prix)), int(prix))
# text = "Il s'appelle {}, et il a {} ans. Il est venu faire un achat pour {} euros"
# print(text.format(nom +' '+ prenom, age, prix))

""" 
# format()
    format() permet d'insérer des valeurs dans les accolades d'un texte suivant l'ordre des paramètres passés. 

    Exemple: print(text.format(nom +' '+ prenom, age, prix)) // Il s'appelle AZANKPO Erik, et il a 20 ans. Il est venu faire un achat pour 15 euros
"""

# nomJoueur = input("Veuillez entrer votre nom: ")
# print("Bienvenue,", nomJoueur)

"""
#input()
    input() permet de récupérer toutes les informations requises renseignées par l'utilisateur

    Exemple: nomJoueur = input("Veuillez entrer votre nom: ") // Ça affichera à l'utilisateur: Veuillez entrer votre nom: 

"""

# user_id_register = "erik.azankpo"
# user_pwd_register = "eric2024."
# nom = user_id_register.split(".")[0].capitalize()
# prenom = user_id_register.split(".")[1].capitalize()

# print("Page de connexion")
# user_id = input("Veuillez entrer votre identifiant: ")
# user_pwd = input("Veuillez entrer votre mot de passe: ")

# if user_id == user_id_register and user_pwd == user_pwd_register:
#     print("Bienvenue sur la page", nom , prenom)
# elif user_id != user_id_register and user_pwd == user_pwd_register:
#     print("L'identifiant entré est incorrect")
# elif user_id == user_id_register and user_pwd != user_pwd_register:
#     print("Le mot de passe entré est incorrect")
# else:
#     print("L'identifiant et le mot de passe entrés sont incorrects")


# age = input("Veuille entrer votre âge: ")
# age = int(age)
# if age >= 80:
#     print("Oups! Vous avez {} ans, vous êtes vieux, vous ne pouvez plus avoir accès à la salle de fête...".format(age))
# elif age >= 18:
#     print("Oh super! Vous venez d'avoir {} ans, vous êtes jeune et majeur, veuillez entrer à la salle de fête...".format(age))
# else: 
#     print("Oh purée! Vous n'avez pas encore l'âge d'avoir accès à la salle de fête...".format(age))


""" 
    Au lieu de mettre multiple condition comme suite:
        if age > 0 and age >= 100
    
    nous pouvons la simplifier:
        0 < age <= 100:
"""
# age = input("Quel est votre âge ?")
# age = int(age)

# if 0 < age <= 19: 
#     print("Vous n'avez pas encore 20 ans")
# else:
#     print("Vous avez déjà 20 ans")
    
    
# condition = "Oui"

# demande = input("Etes-vous d'accord ?")

# # if demande != condition:
# #     demande = input("Etes-vous d'accord ?")
# # else :
# #     print("Super, vous avez pris la bonne décision😅")
    
# while condition:
#     demande = input("Etes-vous d'accord ?")
# if demande : 
#     print("Super, vous avez pris la bonne décision😅")
    
    
# compteur = 0

# while compteur <= 5:
#     print("Compteur : ",compteur )
#     compteur += 1

# jeu_lance = True
# niveau = 0

# print("Bienvenue dans JUMANJI")
# print("Appuyer sur:")
# print("1- reprendre le jeu")
# print("2- recommencer à partir du début")
# print("3- changer de niveau")

# while jeu_lance:
#     choixMenu = input("> ")
#     choixMenu = int(choixMenu)
#     if choixMenu == 1:
#         print("Le jeu reprend dans 30 secondes")
#     elif choixMenu == 2:
#         print("Etes-vous sûr de vouloir reprendre le jeu ?")
#         print("1- Oui")
#         print("2- Non")
#         choixMenu2 = input("> ")
#         choixMenu2 = int(choixMenu2)
#         if choixMenu2 == 1:
#             print("Le jeu recommence dans 30 secondes")
#         else:
#             continue
#     elif choixMenu == 3:
#         print("Niveaux disponibles: ")
#         while niveau <5:
#             print("Niveaux ", niveau)
#             niveau += 1
#         choixMenu3 = input("> ")
#         choixMenu3 = int(choixMenu3)
#         break
#      else:
#         print("Veuillez entrer le bon chiffre")

# t = input("Veuillez taper le temps : ")
# d = input("Veuillez taper la distance : ")

# t = float(t)
# d = float(d)

# while t>d:
# 	print ("Veuillez entrer un temps inférieur à la distance")
# 	t = input("Veuillez taper le temps : ")
# 	d = input("Veuillez taper la distance : ")
# 	t = float(t)
# 	d = float(d)
# if t<=d:
# 	vitesse = d / t 
# 	vitesse = float(vitesse)

# print ("la valeur de la vitesse est de :", vitesse)
# print ("\n vitesse = {:.4}KM/H".format(vitesse))

# def dire_bonjour(nom = "Tom"):
#     print("Bonjour,",nom)
    
# dire_bonjour()

# def requete():
#     print("1. Faire une addition")
#     print("2. Faire une soustration")
#     print("3. Faire une multiplication")
#     print("4. Faire une division")

# # requete()
# def calcul(nombre1, signe, nombre2):
#     if signe == "/":
#         return int(nombre1) / int(nombre2) 
#     elif signe == "-":
#         return int(nombre1) - int(nombre2) 
#     elif signe == "+":
#         return int(nombre1) + int(nombre2) 
#     else:
#         return int(nombre1) * int(nombre2) 
        
    
# print(int(calcul(12, "/" , 2)))
# jeu_lance = True

# while jeu_lance:
#     requete()
#     variable = int(input("> "))
#     if variable == 1:
#         print("Entrez le chiffre 1:")
#         nombre1 = int(input("> "))
#         print("Entrez le chiffre 2:")
#         nombre2 = int(input("> "))
        
# taxe = lambda prix: prix + (prix * 20/100)

# print(taxe(10))


"""
Un module est fichier dans lequel certains fonction spécifiques ont été développées et sont prêtes à être importées pour l'utilisation
    
Pour utiliser une fonction d'un module, il faut d'abord importer le fichier en question
    
Exemple: 
import math 

resultat = math.sqrt(100)
print(int(resultat))


import os

os.system("cls") // Cela agira sur le terminal du système
"""

# import player

# import math 

# r = player.parler("Serge", "Bonjour")


# try:
#     print("Quel âge as-tu ?")
#     age = int(input("> "))
# except:
#     print("L'âge entré n'est pas correct")
# else:
#     print("Vous avez {} ans".format(age))
# finally:
#     print("FIN DU PROGRAMME")


# print("Quel âge as-tu ?")
# age = int(input("> "))

# if type(age) != int: 
#     print("L'âge entré est incorrect")
# else: 
#     print("Vous avez {} ans".format(age))
    
    
"""
Il est possible de créer les exceptions soi-même en utilisant le mot clé raise

Exemple:
age = int(input("> "))
if age < 25:
    raise ValueError("Age must be above 25")
else: 
    print(age)

"""

# print("Quel âge as-tu ?")

# age = input("> ")

# try:
#     age = int(age)
#     assert age > 17
# except:
#     print("Une erreur est survenue lors de l'opération")
# else:
#     print("Vous avez {} ans".format(age))

# import Player as Joueur

# humain = Joueur.Player("AZANKPO","Erik")

# humain.nom = "ADEYEMI"
# humain.parler("Erik","Je viens de bouger")

# humain.ecole = "Pigier"
# Joueur.Player.definition("Erikoooooooooooooooo")
# print(humain.ecole)

import Player

Player.Player.method_static()

# print("Bienvenue sur la page...")
# print("Quel est votre prénom ?")
# prenom = input("> ")

# print("Votre message svp...")
# message = input("> ")

# print("Quel est votre âge ?")
# age = input("> ")
# age = int(age)
# try:
#     assert type(age) == int and age >= 18
# except AssertionError:
#     print("L'âge que vous entrez n'est pas correct")
# else:
#     player = Player.Player(prenom, message)
#     player.jouer()

print(Player.Player.new_pro('Votre message svp'))