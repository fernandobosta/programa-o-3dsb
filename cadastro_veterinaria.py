class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

# Exemplo de polimorfismo
def registrar_animal(animal):
    print(f"Registrando animal que faz: {animal.emitir_som()}")

# Uso
rex = Cachorro()
mingau = Gato()

registrar_animal(rex)
registrar_animal(mingau)
