from entidade.animal import Animal
from entidade.doador import Doador
from datetime import date


class Doacao: #RegistroDoacao
    def __init__(self, data_doacao: date, animal: int, doador, motivo: str):
        self.__data_doacao = data_doacao
        self.__animal = animal
        self.__doador = doador
        self.__motivo = motivo

    @property
    def data_doacao(self):
        return self.__data_doacao
    
    @data_doacao.setter
    def data_doacao(self, data):
        self.__data_doacao = data

    @property
    def animal(self):
        return self.__animal
    
    @animal.setter
    def animal(self, animal):
        self.__animal = animal
    
    @property
    def doador(self):
        return self.__doador
    
    @doador.setter
    def doador(self, doador):
        self.__doador = doador
    
    @property
    def motivo(self):
        return self.__motivo
    
    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo
    
