from entidade.animal import Animal
from entidade.doador import Doador
from datetime import date


class Doacao: #RegistroDoacao
    def __init__(self, data_doacao: date, animal: Animal, doador: Doador, motivo: str):
        self.__data_doacao = data_doacao
        self.__animal = animal
        self.__doador = doador
        self.__motivo = motivo

    @property
    def data_doacao(self):
        return self.__data_doacao

    @property
    def animal(self):
        return self.__animal
    
    @property
    def doador(self):
        return self.__doador
    
    @property
    def motivo(self):
        return self.__motivo
    
    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo
    
