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
        if animal not in self.listar_animais_disponiveis():
            self.__doacoes.append(Doacao(data_doacao, animal, doador, motivo))
            self.__animais.append(animal)

    def registrar_adocao(self, data_adocao: date, animal: Animal, adotante: Adotante, termo_resp: bool):
        if (not adotante.data_nascimento < date.today().strftime('2006/%m/%d') #Se não é 18-
        and adotante.tipo_habitacao == 'Apartamento pequeno' #E apartamento pequeno
        and animal.__class__ == Cachorro and animal.tamanho == 'G'): #Com cachorro grande

            vacinas_necessarias = ['Raiva', 'Leptospirose', 'Hepatite Infecciosa']
            tem_vacinas = 0

            for vacina in vacinas_necessarias:
                if vacina in animal.vacinas:
                    tem_vacinas += 1

            if tem_vacinas == 3: #E tem as vacinas necessárias

                nao_doou = True
                for doacao in self.doacoes:
                    if adotante.cpf == doacao.doador.cpf:
                        nao_doou = False

                if nao_doou: #E nunca doou um animal
                    #A adoção é liberada
                    self.__adocoes.append(Adocao(data_adocao, animal, adotante, termo_resp))
