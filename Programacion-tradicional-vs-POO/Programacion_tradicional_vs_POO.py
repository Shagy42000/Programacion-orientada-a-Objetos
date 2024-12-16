# Programación Tradicional

def ingresar_temperaturas(entradas):
    """
    Recibe una lista de temperaturas predefinidas y las retorna.
    """
    return entradas  # Devuelve la lista de temperaturas predefinidas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)  # Suma todas las temperaturas y las divide entre el número de elementos

# Flujo principal del programa
if __name__ == "__main__":
    print("Bienvenido al programa de cálculo del promedio semanal de temperaturas (Programación Tradicional).")
    temperaturas = [21.5, 22.3, 20.1, 19.8, 23.2, 24.5, 25.0]  # Temperaturas predefinidas para prueba
    print(f"Las temperaturas ingresadas son: {temperaturas}")  # Muestra la lista de temperaturas ingresadas
    promedio = calcular_promedio(temperaturas)  # Calcula el promedio de las temperaturas ingresadas
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")  # Muestra el promedio calculado


# Programación Orientada a Objetos

class ClimaSemanal:
    """
    Clase que representa el clima semanal.
    Permite almacenar las temperaturas diarias y calcular el promedio semanal.
    """
    def __init__(self, temperaturas):
        self.temperaturas = temperaturas  # Atributo para almacenar temperaturas predefinidas

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio semanal de temperaturas.
        """
        return sum(self.temperaturas) / len(self.temperaturas)  # Suma todas las temperaturas y las divide entre el número de elementos

# Flujo principal del programa
if __name__ == "__main__":
    print("Bienvenido al programa de cálculo del promedio semanal de temperaturas (POO).")
    temperaturas = [21.5, 22.3, 20.1, 19.8, 23.2, 24.5, 25.0]  # Temperaturas predefinidas para prueba
    clima = ClimaSemanal(temperaturas)  # Crea una instancia de la clase ClimaSemanal con temperaturas predefinidas
    print(f"Las temperaturas ingresadas son: {clima.temperaturas}")  # Muestra la lista de temperaturas almacenadas en la instancia
    promedio = clima.calcular_promedio()  # Calcula el promedio de las temperaturas ingresadas
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")  # Muestra el promedio calculado
