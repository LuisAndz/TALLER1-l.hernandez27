class Perro:

    def __init__(self, nombre: str, raza: str, peso: float, edad: int):
        self.__nombre = nombre  # ._ lo convierte en privado
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        # self.__concentrado_pref=concentrado_pref

    def ladrar(self):
        print(f"\nGuau guau dijo {self.__nombre}")

    def cambio_peso(self, nuevo_peso: float):
        self.__peso = nuevo_peso

    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    def get_concentrado(self):
        return self.__concentrado_pref

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_raza(self, nueva_raza):
        self.__raza = nueva_raza

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

    def set_peso(self, nuevo_peso):
        self.__peso = nuevo_peso

    def set_concentrado(self, nuevo_concentrado):
        self.__concentrado_pref = nuevo_concentrado

    def get_dict_attributes(self):
        return self.__dict__
