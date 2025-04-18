from models.perro import Perro


class Guarderia:
    def __init__(self, nombre: str, ubicacion: str):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__perros = [{"nombre": "Rufo", "raza": "Labrador", "peso": 22, "edad": 7},
                         {"nombre": "Bingo", "raza": "Pug", "peso": 6, "edad": 2},
                         {"nombre": "Lassie", "raza": "collie", "peso": 27, "edad": 5}]

    def add_perros(self, perro: Perro):
        self.__perros.append(perro)

    def retornar_perros(self):
        return tuple(self.__perros)

    def get_nombre(self):
        return self.__nombre

    def get_ubicacion(self):
        return self.__ubicacion

    def set_nombre(self, neo_nombre: str):
        self.__nombre = neo_nombre

    def set_ubicacion(self, neo_ubicacion: str):
        self.__ubicacion = neo_ubicacion


if __name__ == "__main__":

    guarderia1 = Guarderia("Patitas", "Av. Siempre viva loc. 109")
    print(guarderia1.retornar_perros())
