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


# class Player:
#     propriete_de_la_classe = "Je suis la propriété de la classe"
    
#     def __init__(self, nom, prenom):
#         self.nom = nom
#         self.prenom = prenom
#         print(Player.propriete_de_la_classe)
        
#     def jouer(self):
#         print(self.nom, self.prenom) 
        
#     def method_static():
#         print("Je suis une méthode statique")
    
#     method_static = staticmethod(method_static)
#     def changement_de_propriete(cls, nouvelle_propriete):
#         Player.propriete_de_la_classe = nouvelle_propriete
        
#     new_pro = classmethod(changement_de_propriete)

class Player:
    
    variable_de_la_propriete = "Valeur par défaut"
    def __init__(self, nom, prenom,age):
        self.nom = nom
        self.prenom = prenom
        self._age = age
        # print(Player.variable_de_la_propriete)
        
    def methode_de_nouvelle_valeur(cls, nouvelle_valeur):
        Player.variable_de_la_propriete = nouvelle_valeur
        
    new = classmethod(methode_de_nouvelle_valeur)
    
    def _getAge(self):
        return self._age
    
    def _setAge(self, age):
        self._age = age
        
    def _delAge(self):
        del self._age
    
    newAge = property(_getAge, _setAge, _delAge)
    