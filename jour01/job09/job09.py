class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        print(f"Produit : {self.nom}\nPrix HT : {self.prixHT} €\nTVA : {self.TVA}%\nPrix TTC : {self.CalculerPrixTTC()} €")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

# Instanciation de plusieurs produits.
produit1 = Produit(nom="Livre", prixHT=15, TVA=5)
produit2 = Produit(nom="Machien a vaisselle", prixHT=800, TVA=20)
produit3 = Produit(nom="Télévision", prixHT=500, TVA=10)

# Affichage des informations initiales concernant les produits.
print("Informations initiales des produits :")
produit1.afficher()
produit2.afficher()
produit3.afficher()

# changement du nom et du prix de chaque produit.
produit1.modifierNom("Roman")
produit1.modifierPrixHT(12)

produit2.modifierNom("Laptop")
produit2.modifierPrixHT(750)

produit3.modifierNom("TV LED")
produit3.modifierPrixHT(450)

# Affichage des informations mises à jour concernant les produits.
print("\nInformations des produits après modification :")
produit1.afficher()
produit2.afficher()
produit3.afficher()
