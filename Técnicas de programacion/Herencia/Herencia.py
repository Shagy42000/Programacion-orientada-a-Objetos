# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Subclase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()}, Número de puertas: {self.num_puertas}"

# Subclase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.tipo = tipo

    def descripcion(self):
        return f"{super().descripcion()}, Tipo: {self.tipo}"

# Crear instancias de Coche y Moto
mi_coche = Coche("Toyota", "Corolla", 4)
mi_moto = Moto("Yamaha", "MT-07", "Deportiva")

# Utilizar el método descripcion para imprimir los detalles
print(mi_coche.descripcion())  # Salida: Marca: Toyota, Modelo: Corolla, Número de puertas: 4
print(mi_moto.descripcion())   # Salida: Marca: Yamaha, Modelo: MT-07, Tipo: Deportiva
