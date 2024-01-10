class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"L'âge de l'animal {self.prenom} est {self.age} an(s)")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}")

# Création d'une instance de la classe Animal.
animal_instance = Animal()

# Affichage de l'âge initial de l'animal.
animal_instance.afficherAge()

# Augmentation de l'âge de l'animal et affichage de son nouvel âge après le processus de vieillissement.
animal_instance.vieillir()
print("# Age de l'animal après appel de la méthode vieillir")
animal_instance.afficherAge()

# Attribution d'un nom à l'animal et affichage d'un nom ainsi défini.
animal_instance.nommer("Luna")
