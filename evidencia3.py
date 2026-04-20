class Persona:
    pass
class Persona:
    def __init__(self, nombre, edad, altura, peso, correo):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
        self.__correo = correo
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad
        def set_nombre(self, nombre):
            self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad
    def calcular_imc(self):
        return self.__peso / (self.__altura ** 2)
    def es_mayor_de_edad(self):
        return self.__edad >= 18
        def info(self):
            return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Correo: {self.__correo}"
        persona1 = Persona("Ezequiel", 18, 1.75, 70, "correo@gmail.com")

print(persona1.info())
print("IMC:", persona1.calcular_imc())
print("Mayor de edad:", persona1.es_mayor_de_edad())
