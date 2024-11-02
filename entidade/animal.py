from abc import ABC, abstractmethod
from entidade.vacinacao import Vacinacao


class Animal(ABC):

    @abstractmethod
    def __init__(self, num_chip: int, nome: str, raca: str, vacinas = []):
        self.__num_chip = num_chip
        self.__nome = nome
        self.__raca = raca
        self.__vacinas = vacinas

    @property
    def num_chip(self):
        return self.__num_chip
    
    @num_chip.setter
    def num_chip(self, num_chip):
        self.__num_chip = num_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def raca(self):
        return self.__raca
    
    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def vacinas(self):
        return self.__vacinas

    def add_vacina(self, vacina: Vacinacao):
        self.__vacinas.append(vacina)

