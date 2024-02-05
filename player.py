class Player:
    def __init__(self, nom = "Dove", prenom = "ddd", age = 88, taille = ''):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille
        
        print("Je suis {} {}, j'ai {} ans et ma taille est {}".format(nom, prenom, age, taille))
    
    # print("Je suis dans la classe Joueur")