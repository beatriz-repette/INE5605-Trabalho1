from entidade.animal import Animal
from entidade.adotante import Adotante
from datetime import date, datetime


class Adocao:
    def __init__(self, data_adocao: datetime,  animal: int, adotante: str, termo_responsabilidade: bool):
        self.__data_adocao = data_adocao
        self.__adotante = adotante
        self.__animal = animal
        self.__termo_responsabilidade = termo_responsabilidade

    @property
    def data_adocao(self):
        return self.__data_adocao
    
    @data_adocao.setter
    def data_adocao(self, data):
        self.__data_adocao = data

    @property
    def animal(self):
        return self.__animal
    
    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def adotante(self):
        return self.__adotante
    
    @adotante.setter
    def adotante(self, adotante):
        self.__adotante = adotante

    @property
    def termo_responsabilidade(self):
        return self.__termo_responsabilidade
    
    @termo_responsabilidade.setter
    def termo_responsabilidade(self, termo_responsabilidade):
        self.__termo_responsabilidade = termo_responsabilidade
