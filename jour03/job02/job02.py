class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom 
        self._prenom = prenom 
        self._solde = solde 
        self._decouvert = decouvert
    
       
    def afficher(self):
        print(f"Compte n°{self._numero_compte} - {self._prenom} {self._nom}")

    def afficherSolde(self):
        print(f"Solde du compte : {self._solde} euros")
    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} euros effectué. Nouveau solde : {self._solde} euros")
    def retrait(self, montant):
        if not self._decouvert and montant > self._solde:
            print("Opération impossible : solde insuffisant.")
        else:
            self._solde -= montant
            print(f"Retrait de {montant} euros effectué. Nouveau solde : {self._solde} euros")
    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * taux_agios
            self._solde -= agios
            print(f"Des agios de {agios} euros ont été appliqués. Nouveau solde : {self._solde} euros")
    def virement(self, compte_destinataire, montant):
        if self._solde >= montant:
            self._solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} euros effectué avec succès.")
        else:
            print("Virement impossible : solde insuffisant.")
 
compte1 = CompteBancaire(numero_compte="899034", nom="Montéro", prenom="Christine", solde=1000)

compte1.afficher()
compte1.afficherSolde()
 

compte1.versement(500)
compte1.retrait(200)
 
compte2 = CompteBancaire(numero_compte="574523", nom="Masoomi", prenom="Ali", solde=-500, decouvert=True)
compte2.afficher()
compte2.afficherSolde()
 
compte1.virement(compte_destinataire=compte2, montant=300)
 
compte2.agios(taux_agios=0.05)
 