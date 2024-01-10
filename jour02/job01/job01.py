class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur  # Attribut privé avec un seul underscore
        self._largeur = largeur    # Attribut privé avec un seul underscore

    # Accesseurs (getters)
    def getLongueur(self):
        return self._longueur

    def getLargeur(self):
        return self._largeur

    # Mutateurs (setters)
    def setLongueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur

# Création d'un rectangle avec les valeurs initiales
rectangle = Rectangle(longueur=10, largeur=5)

# Affichage des valeurs initiales
print("Longueur initiale :", rectangle.getLongueur())
print("Largeur initiale :", rectangle.getLargeur())

# Modification des valeurs
rectangle.setLongueur(15)
rectangle.setLargeur(8)

# Affichage des nouvelles valeurs
print("\nNouvelle longueur :", rectangle.getLongueur())
print("Nouvelle largeur :", rectangle.getLargeur())
