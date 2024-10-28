from datetime import date


class Vacinacao():
    def __init__(self, data: date, vacina: str, animal: int):
        self.__data = data
        self.__vacina = vacina
        self.__animal_chip = animal

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,data):
        self.__data = data

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self,vacina):
        self.__vacina = vacina

    @property
    def animal(self):
        return self.__animal_chip
