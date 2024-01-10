class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
 
    def marquerUnBut(self):
        self.buts_marques += 1
 
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
 
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
 
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
 
    def afficherStatistiques(self):
        print(f"Statistiques pour le joueur {self.nom} ({self.position}, #{self.numero}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print("\n")
 
 
class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []
 
    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
 
    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques pour l'équipe {self.nom} :")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()
 
    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe_decisive":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()
 
 
 
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Harry Kane", 7, "Attaquant")
joueur3 = Joueur("Gavi", 8, "Milieu")
 
equipe1 = Equipe("Argentine")
equipe2 = Equipe("Angleterre")
 
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)
 
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
 
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Di Maria", "passe_decisive")
equipe1.mettreAJourStatistiquesJoueur("Acuna", "carton_jaune")
 
equipe2.mettreAJourStatistiquesJoueur("Harry Kane", "but")
equipe2.mettreAJourStatistiquesJoueur("Saka", "carton_rouge")
 
# Afficher les statistiques après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
 
