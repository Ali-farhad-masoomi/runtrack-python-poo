class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée horizontale x est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée verticale y est : {self.y}")

    def changerX(self, nouveau_x):
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y

# Création d'instances de la classe point avec des valeurs initials définies.
point_instance = Point(x=3, y=5)

# Appel des méthodes pour d'afficher pour montrer les coordonnées iniitiales.
point_instance.afficherLesPoints()
point_instance.afficherX()
point_instance.afficherY()

# Modification des coordonnées en utilisant les méthoodes 'changerX' et 'changerY'.
point_instance.changerX(8)
point_instance.changerY(10)

# Appel des méthodes d'affichage pour montrer les nouvelles coordonnéees.
point_instance.afficherLesPoints()
point_instance.afficherX()
point_instance.afficherY()
