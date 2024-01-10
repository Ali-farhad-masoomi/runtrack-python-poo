class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre  # Attribut privé avec un seul underscore
        self._auteur = auteur  # Attribut privé avec un seul underscore
        self._nombre_pages = nombre_pages  # Attribut privé avec un seul underscore

    # Assesseurs (getters)
    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNombrePages(self):
        return self._nombre_pages

    # Mutateurs (setters)
    def setTitre(self, nouveau_titre):
        self._titre = nouveau_titre

    def setAuteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur

    def setNombrePages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self._nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

# Exemple d'utilisation de la classe Livre
livre = Livre(titre="Gatsby le Magnifique", auteur="F. Scott Fitzgerald", nombre_pages=300)

# Affichage des informations initiales
print("Titre :", livre.getTitre())
print("Auteur :", livre.getAuteur())
print("Nombre de pages :", livre.getNombrePages())

# Modification des valeurs
livre.setTitre("1984")
livre.setAuteur("George Orwell")
livre.setNombrePages(250)  # Modification avec une valeur valide
livre.setNombrePages(-50)  # Tentative de modification avec une valeur invalide

# Affichage des nouvelles valeurs
print("\nNouveau titre :", livre.getTitre())
print("Nouvel auteur :", livre.getAuteur())
print("Nouveau nombre de pages :", livre.getNombrePages())
