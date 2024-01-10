class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50  # Attribut privé réservoir initialisé à 50 par défaut

    # Assesseurs (getters)
    def getMarque(self):
        return self._marque

    def getModele(self):
        return self._modele

    def getAnnee(self):
        return self._annee

    def getKilometrage(self):
        return self._kilometrage

    def getEnMarche(self):
        return self._en_marche

    # Mutateurs (setters)
    def setMarque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def setModele(self, nouveau_modele):
        self._modele = nouveau_modele

    def setAnnee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def setKilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    # Méthode privée pour vérifier le niveau du réservoir
    def _verifier_plein(self):
        return self._reservoir > 5

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2022, kilometrage=15000)

# Affichage des informations initiales
print("Marque :", ma_voiture.getMarque())
print("Modèle :", ma_voiture.getModele())
print("Année :", ma_voiture.getAnnee())
print("Kilométrage :", ma_voiture.getKilometrage())
print("En marche :", ma_voiture.getEnMarche())

# Modification des attributs
ma_voiture.setMarque("Honda")
ma_voiture.setModele("Civic")
ma_voiture.setAnnee(2020)
ma_voiture.setKilometrage(20000)

# Démarrage de la voiture (si le réservoir est suffisant)
ma_voiture.demarrer()

# Affichage de l'état après démarrage
print("En marche :", ma_voiture.getEnMarche())

# Arrêt de la voiture
ma_voiture.arreter()

# Affichage de l'état après arrêt
print("En marche :", ma_voiture.getEnMarche())
