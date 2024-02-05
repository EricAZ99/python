# class Player:
    
#     ecole = "Nokoué"
    
#     def __init__(self, nom = "Dove", prenom = "ddd", age = 88, taille = ''):
#         self.nom = nom
#         self.prenom = prenom
#         self.age = age
#         self.taille = taille
        
#         # print("Je suis {} {}, j'ai {} ans et ma taille est {}".format(nom, prenom, age, taille))
    
#     # print("Je suis dans la classe Joueur") 
#     def parler(self, nom, message):
#         print("{} a dit : {}".format(nom, message))
        
#     def changement_d_ecole(cls, nouvelle_ecole):
#         Player.ecole = nouvelle_ecole
    
#     eleve = classmethod(changement_d_ecole)
    
#     @staticmethod
#     def definition(message):
#         print("{}".format(message))


class Player:
    propriete_de_la_classe = "Je suis la propriété de la classe"
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        print(self.nom, Player.propriete_de_la_classe)
        
    def jouer(self):
        print(self.nom, self.prenom) 
        
    def method_static():
        print("Je suis une méthode statique")
        
    
