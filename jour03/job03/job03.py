class Tache:
    def __init__(self, titre, description, statut="À Réaliser !"):
        self.titre = titre
        self.description = description
        self.statut = statut
    def __str__(self):
        return f"{self.titre} - {self.description} - Statut: {self.statut}"
 
 
class ListeDeTaches:
    def __init__(self):
        self.taches = []
 
    def ajouterTache(self, tache):
        self.taches.append(tache)
 
    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]
 
    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
 
    def afficherListe(self):
        for tache in self.taches:
            print(tache)
 
    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]
 
 
# Test du code
tache1 = Tache("Natation", "Running")
tache2 = Tache("Apprendre", "Voyager")
tache3 = Tache("Faire des courses", "Tache ménagère")
 
liste_taches = ListeDeTaches()
 
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)
 
# Afficher la liste des tâches
print("Liste des tâches:")
liste_taches.afficherListe()
 
 
liste_taches.marquerCommeFinie("Running")
 
print("Liste des tâches après marquerCommeFinie:")
liste_taches.afficherListe()
 
liste_taches.supprimerTache("Tache ménagère")
 
print("Liste des tâches après supprimerTache:")
liste_taches.afficherListe()
 
taches_a_faire = liste_taches.filterListe("À réaliser")
print("Liste des tâches à faire:")
for tache in taches_a_faire:
    print(tache)
 