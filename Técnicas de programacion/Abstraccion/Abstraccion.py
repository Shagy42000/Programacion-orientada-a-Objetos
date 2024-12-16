from abc import ABC, abstractmethod

# Definimos una clase abstracta llamada Animal que hereda de ABC (Abstract Base Class)
class Animal(ABC):
    # Método abstracto que deben implementar todas las subclases
    @abstractmethod
    def hacer_sonido(self):
        # Esta es una declaración de método abstracto. No tiene implementación aquí.
        pass

# Definimos la clase Perro que hereda de Animal
class Perro(Animal):
    # Implementamos el método hacer_sonido
    def hacer_sonido(self):
        # Devolvemos el sonido específico del perro
        return "Guau"

# Definimos la clase Gato que hereda de Animal
class Gato(Animal):
    # Implementamos el método hacer_sonido
    def hacer_sonido(self):
        # Devolvemos el sonido específico del gato
        return "Miau"

# Creamos una instancia de la clase Perro
mi_perro = Perro()
# Creamos una instancia de la clase Gato
mi_gato = Gato()

# Llamamos al método hacer_sonido de la instancia mi_perro y imprimimos el resultado
print(mi_perro.hacer_sonido())  # Salida: Guau
# Llamamos al método hacer_sonido de la instancia mi_gato y imprimimos el resultado
print(mi_gato.hacer_sonido())   # Salida: Miau
