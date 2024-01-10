class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
 
    def longueur(self):
        return self._longueur
 
    def longueur(self, value):
        self._longueur = value
 
    def largeur(self):
        return self._largeur
 
    def largeur(self, value):
        self._largeur = value
    def perimetre(self):
        return 2 * (self._longueur + self._largeur)
 
    def surface(self):
        return self._longueur * self._largeur
 
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
# Propriété et Mutateur pour hauteur: Ces méthodes permettent d'accéder à l'attribut hauteur de manière contrôlée.
    def hauteur(self):
        return self._hauteur
 
    def hauteur(self, value):
        self._hauteur = value
# Cette méthode calcule le volume du parallélépipède en utilisant les valeurs des attributs longueur, largeur et hauteur.
    def volume(self):
        return self._longueur * self._largeur * self._hauteur
 
 

rectangle1 = Rectangle(longueur=8, largeur=5)
 
# Affichage de la surface et du périmètre du rectangle
print("Rectangle - Surface:", rectangle1.surface())
print("Rectangle - Périmètre:", rectangle1.perimetre())
 
# Modification des dimensions du rectangle à l'aide des mutateurs
rectangle1.longueur = 6
rectangle1.largeur = 3
 
# Affichage des nouvelles dimensions, surface et périmètre du rectangle
print("Nouvelles dimensions du rectangle:")
print("Longueur:", rectangle1.longueur)
print("Largeur:", rectangle1.largeur)
print("Rectangle - Surface:", rectangle1.surface())
print("Rectangle - Périmètre:", rectangle1.perimetre())
 
parallelepipede1 = Parallelepipede(longueur=3, largeur=2, hauteur=4)
 
# Affichage de la surface, du périmètre et du volume du parallélépipède
print("\nParallélépipède - Volume:", parallelepipede1.volume())
 