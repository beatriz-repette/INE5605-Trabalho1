from animal import Animal
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

    def listar_animais_disponiveis(self):
        disponiveis = self.__animais
        for animal in self.__animais:
            for adocao in self.__adocoes:
                if animal.num_chip == adocao.animal.num_chip:
                    disponiveis.remove(animal)
        return disponiveis

    def registrar_doacao(self, doador: Doador, animal: Animal, data_doacao: date, motivo: str):
        self.__doacoes.append(Doacao(doador, animal, data_doacao, motivo))
        self.__animais.append(animal)

    def registrar_adocao(self, adotante: Adotante, animal: Animal, data_adocao: date, termo_resp: bool):
        self.__adocoes.append(Adocao(adotante, animal, data_adocao, termo_resp))

