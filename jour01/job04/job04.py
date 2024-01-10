class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Différentes méthodes d'instruction fournies à plusieurs personnes avec des configurations variables.
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Se présenter pour chaque personne.
presentation1 = personne1.SePresenter()
presentation2 = personne2.SePresenter()

# Impression des présentations en console.
print(presentation1)
print(presentation2)
