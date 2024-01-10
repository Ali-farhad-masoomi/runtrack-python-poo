class Student:
    def __init__(self, nom, prenom, id_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._id_etudiant = id_etudiant
        self._credits = 0
        self._level = self._studentEval()  # Initialisation du niveau avec la méthode studentEval

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._studentEval()  # Mise à jour du niveau après ajout de crédits
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom = {self._nom}\nPrénom = {self._prenom}\nIdentifiant = {self._id_etudiant}\nNiveau = {self._level}")

# Instanciation d'un objet représentant l'étudiant John Doe avec le numéro d'étudiant 145
john_doe = Student(nom="Doe", prenom="John", id_etudiant=145)

# Ajout de crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)

# Affichage du total de crédits et des informations de l'étudiant
print(f"Le nombre de crédits de {john_doe._prenom} {john_doe._nom} est de {john_doe._credits} points.")
john_doe.studentInfo()
