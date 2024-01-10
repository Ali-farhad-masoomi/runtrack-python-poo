class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages
        self._disponible = True  # Nouvel attribut privé par défaut à True

    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNombrePages(self):
        return self._nombre_pages

    def isDisponible(self):
        return self._disponible

    def emprunter(self):
        if self.isDisponible():
            print("Emprunt du livre.")
            self._disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.isDisponible():
            print("Le livre a été rendu.")
            self._disponible = True
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation de la classe Livre avec les nouvelles fonctionnalités
livre = Livre(titre="Gatsby le Magnifique", auteur="F. Scott Fitzgerald", nombre_pages=300)

# Vérification de la disponibilité initiale
print("Le livre est disponible :", livre.isDisponible())

# Emprunt du livre
livre.emprunter()

# Tentative d'emprunt du livre déjà emprunté
livre.emprunter()

# Rendre le livre
livre.rendre()

# Tentative de rendre un livre déjà disponible
livre.rendre()
