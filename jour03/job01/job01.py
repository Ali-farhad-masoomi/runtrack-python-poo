class Ville:
    def __init__(self, nom, nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants

    def get_population(self):
        return self._nombre_habitants
    def augmenter_population(self, nombre):
        self._nombre_habitants += nombre

class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville
        self._ville.augmenter_population(1)
    def ajouter_population(self):
        self._ville.augmenter_population(1)
 
 

paris = Ville("Paris", 1000000)
# Afficher en console le nombre d’habitants de la ville de Paris.
print(f"Population de la ville de Paris : {paris.get_population()} habitants")
 
# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
marseille = Ville("Marseille", 861635)
# Afficher en console le nombre d’habitants de la ville de Marseille.
print(f"Population de la ville de Marseille : {marseille.get_population()} habitants")

john = Personne("John", 45, paris)

myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)
 
# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
print(f"Mise à jour de la population de la ville de Paris : {paris.get_population()} habitants")
print(f"Mise à jour de la population de la ville de Marseille : {marseille.get_population()} habitants")
 