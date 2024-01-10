class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if self._statut_commande == "en cours":
            if nom_plat not in self._plats_commandes:
                self._plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
                print(f"Plat ajouté à la commande : {nom_plat}")
            else:
                print("Ce plat est déjà dans la commande.")
        else:
            print("Impossible d'ajouter un plat, la commande n'est plus en cours.")

    def annuler_commande(self):
        if self._statut_commande == "en cours":
            self._plats_commandes = {}
            self._statut_commande = "annulée"
            print("Commande annulée.")
        else:
            print("Impossible d'annuler la commande, elle n'est plus en cours.")

    def _calculer_total(self):
        total = sum(plat["prix"] for plat in self._plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande n°{self._numero_commande}")
        for plat, details in self._plats_commandes.items():
            print(f"{plat} - Prix : {details['prix']} € - Statut : {details['statut']}")
        print(f"Total à payer : {self._calculer_total()} €")

    def calculer_tva(self, taux_tva):
        total_tva = self._calculer_total() * (taux_tva / 100)
        return total_tva

# Exemple d'utilisation de la classe Commande
commande1 = Commande(numero_commande=1)

# Ajout de plats à la commande
commande1.ajouter_plat(nom_plat="Pizza", prix_plat=10)
commande1.ajouter_plat(nom_plat="Burger", prix_plat=8.5)
commande1.ajouter_plat(nom_plat="Salade", prix_plat=5)

# Affichage de la commande
commande1.afficher_commande()

# Calcul de la TVA
taux_tva = 10  # Exemple de taux de TVA
total_tva = commande1.calculer_tva(taux_tva)
print(f"Total TVA : {total_tva} €")

# Annulation de la commande
commande1.annuler_commande()

# Affichage de la commande après annulation
commande1.afficher_commande()
