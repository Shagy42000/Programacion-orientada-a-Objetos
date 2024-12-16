class Temperatura:
    # Constructor para inicializar la temperatura en grados Celsius
    def __init__(self, celsius):
        self.__celsius = celsius  # Atributo privado

    # Método para obtener la temperatura en grados Celsius (getter)
    def obtener_celsius(self):
        return self.__celsius

    # Método para configurar la temperatura en grados Celsius (setter)
    def configurar_celsius(self, celsius):
        if -273.15 <= celsius:  # Verificamos que la temperatura no sea menor al cero absoluto
            self.__celsius = celsius
        else:
            print("La temperatura no puede ser menor que -273.15 grados Celsius.")

    # Método para obtener la temperatura en grados Fahrenheit (getter)
    def obtener_fahrenheit(self):
        return self.__celsius * 9/5 + 32

    # Método para configurar la temperatura en grados Fahrenheit (setter)
    def configurar_fahrenheit(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        if -273.15 <= celsius:  # Verificamos que la temperatura convertida no sea menor al cero absoluto
            self.__celsius = celsius
        else:
            print("La temperatura no puede ser menor que -459.67 grados Fahrenheit.")

# Crear una instancia de Temperatura
mi_temperatura = Temperatura(25)  # 25 grados Celsius

# Utilizar los métodos para interactuar con los atributos privados
print("Temperatura en Celsius:", mi_temperatura.obtener_celsius())        # Salida: 25
print("Temperatura en Fahrenheit:", mi_temperatura.obtener_fahrenheit())  # Salida: 77.0

# Configurar una nueva temperatura en grados Celsius
mi_temperatura.configurar_celsius(30)
print("Nueva temperatura en Celsius:", mi_temperatura.obtener_celsius())  # Salida: 30

# Configurar una nueva temperatura en grados Fahrenheit
mi_temperatura.configurar_fahrenheit(86)
print("Nueva temperatura en Celsius:", mi_temperatura.obtener_celsius())  # Salida: 30.0
