class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation d'une classe.
operation_instance = Operation(nombre1=12, nombre2=3)

# Impression des valeurs des propriétés en console;
print("Le nombre1 est", operation_instance.nombre1)
print("Le nombre2 est", operation_instance.nombre2)
