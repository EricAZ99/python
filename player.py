class Player:
    
    ecole = "Nokoué"
    
    def __init__(self, nom = "Dove", prenom = "ddd", age = 88, taille = ''):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille
        
        # print("Je suis {} {}, j'ai {} ans et ma taille est {}".format(nom, prenom, age, taille))
    
    # print("Je suis dans la classe Joueur") 
    def parler(self, nom, message):
        print("{} a dit : {}".format(nom, message))
        
    def changement_d_ecole(cls, nouvelle_ecole):
        Player.ecole = nouvelle_ecole
    
    eleve = classmethod(changement_d_ecole)
    
    @staticmethod
    def definition(message):
        print("{}".format(message))