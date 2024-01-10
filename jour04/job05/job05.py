import math
 
class Forme:
    def aire(self):
        return 0
 
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
 
    def aire(self):
        return self.largeur * self.hauteur
   
# La classe Cercle hérite de la classe Forme :
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    def aire(self):
        return math.pi * self.radius ** 2

rectangle1 = Rectangle(largeur=9, hauteur=6)
 
# Affichage de l'aire du rectangle
print("Aire du rectangle:", rectangle1.aire())
 
# Instanciation de la classe Cercle
cercle1 = Cercle(radius=4)
 
# Affichage de l'aire du cercle
print("Aire du cercle:", cercle1.aire())
 