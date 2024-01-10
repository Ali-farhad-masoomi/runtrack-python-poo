import random


class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats
       
class Jeu:
    def __init__(self):
        self.niveau = 1
    def choisirNiveau(self):
        self.niveau = int(input("Selectionner un niveau de difficulté (1, 2, 3) : "))
 
    def lancerJeu(self):
        print(f"Vous avez choisi le niveau de difficulté : {self.niveau}.")
 
        joueur = Personnage("Joueur", 100 * self.niveau)
        ennemi = Personnage("Ennemi", 50 * self.niveau)
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été battu!")
                break
 
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu. Vous avez perdu.")
                break
 
            print(f"{joueur.nom} - Points de vie restants: {joueur.vie}")
            print(f"{ennemi.nom} - Points de vie restants: {ennemi.vie}\n")
 
        if joueur.vie > 0:
            print("Félicitations! Vous avez gagné!.")
        elif ennemi.vie > 0:
            print("Game Over! Vous avez été vaincu.")
 
# Création d'une instance de la classe Jeu.
jeu = Jeu()
 
# Choix du niveau par le joueur.
jeu.choisirNiveau()
 
# Lancement du jeu.
jeu.lancerJeu()
 