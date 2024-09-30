from animal import Animal
from adotante import Adotante
from datetime import date


class Adocao:
    def __init__(self, data_adocao,  animal: Animal, adotante: Adotante, termo_responsabilidade):
        self.__data_adocao = data_adocao
        self.__adotante = adotante
        self.__animal = animal
        self.__termo_responsabilidade = termo_responsabilidade

    @property
    def data_adocao(self):
        return self.__data_adocao

    @property
    def animal(self):
        return self.__animal

    @property
    def adotante(self):
        return self.__adotante

    @property
    def termo_responsabilidade(self):
        return self.__termo_responsabilidade
    
    @termo_responsabilidade.setter
    def termo_responsabilidade(self, termo_responsabilidade):
        self.__termo_responsabilidade = termo_responsabilidade
