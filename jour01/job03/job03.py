class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", resultat)

# Instanciation d'une classe.
operation_instance = Operation(nombre1=12, nombre2=3)

# utilisation de la méthode addition.
operation_instance.addition()
