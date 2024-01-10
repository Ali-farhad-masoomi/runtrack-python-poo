class Personne:
    def __init__(self, age=15):
        self.age = age
 
    def afficherAge(self):
        print(f"L'âge de la personne est de {self.age} ans.")
 
    def bonjour(self):
        print("Hello")
 
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age
 

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
 
    def afficherAge(self):
        print(f"J'ai {self.age} ans.")
 
class Professeur(Personne):
    def __init__(self, age=40, matiere_enseignee=""):
        super().__init__(age)
        self.matiereEnseignee = matiere_enseignee
 
    def enseigner(self):
        print(f"Le cours de {self.matiereEnseignee} va commencer.")
 
personne1 = Personne()
personne1.afficherAge()  
personne1.bonjour()    
 
# Instanciation Eleve :
eleve1 = Eleve()  
eleve1.allerEnCours()  
 
# Instanciation d'un Professeur
professeur1 = Professeur(age=40, matiere_enseignee="Physique")
professeur1.bonjour()    # Affiche "Hello"
professeur1.enseigner()  
 
 
 
 
  
 
 
 