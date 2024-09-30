from animal import Animal
from cachorro import Cachorro
from gato import Gato
from doador import Doador
from adotante import Adotante
from doacao import Doacao
from adocao import Adocao
from datetime import date


class Sistema():
    def __init__(self):
        self.__animais = []
        self.__doacoes = []
        self.__adocoes = []

    @property
    def doacoes(self):
        return self.__doacoes
    
    @property
    def adocoes(self):
        return self.__adocoes

    def listar_animais_disponiveis(self):
        disponiveis = self.__animais
        for animal in self.__animais:
            for adocao in self.__adocoes:
                if animal.num_chip == adocao.animal.num_chip:
                    disponiveis.remove(animal)
        return disponiveis

    def registrar_doacao(self, data_doacao: date, animal: Animal, doador: Doador, motivo: str):
        self.__doacoes.append(Doacao(data_doacao, animal, doador, motivo))
        self.__animais.append(animal)

    def registrar_adocao(self, data_adocao: date, animal: Animal, adotante: Adotante, termo_resp: bool):
        self.__adocoes.append(Adocao(data_adocao, animal, adotante, termo_resp))



