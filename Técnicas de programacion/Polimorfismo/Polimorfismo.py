# Clase base Instrumento
class Instrumento:
    def tocar(self):
        # Este método será sobrescrito en las subclases
        pass

# Subclase Guitarra que hereda de Instrumento
class Guitarra(Instrumento):
    def tocar(self):
        # Implementa el método tocar para la guitarra
        return "Tocando un solo de guitarra"

# Subclase Piano que hereda de Instrumento
class Piano(Instrumento):
    def tocar(self):
        # Implementa el método tocar para el piano
        return "Tocando una melodía en el piano"

# Lista de instrumentos
instrumentos = [Guitarra(), Piano(), Guitarra()]

# Utilizar el polimorfismo para tocar todos los instrumentos en la lista
for instrumento in instrumentos:
    print(instrumento.tocar())
