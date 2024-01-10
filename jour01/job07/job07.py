class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage.
personnage = Personnage(x=3, y=4)

# Affichage de la position initiale.
print("Position initiale :", personnage.position())

# Déplacement vers la droite.
personnage.droite()
print("Position après déplacement vers la droite :", personnage.position())

# Déplacement vers le bas.
personnage.bas()
print("Position après déplacement vers le bas :", personnage.position())
