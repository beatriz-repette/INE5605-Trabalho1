from entidade.pessoa import Pessoa
from datetime import date


class Adotante(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str, tipo_habitacao: str, possui_animal: bool):
        super().__init__(cpf, nome, data_nascimento, endereco)
        self.__tipo_habitacao = tipo_habitacao
        self.__possui_animal = possui_animal

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao
    
    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao):
        self.__tipo_habitacao = tipo_habitacao

    @property
    def possui_animal(self):
        return self.__possui_animal
    
    @possui_animal.setter
    def possui_animal(self, possui_animal):
        self.__possui_animal = possui_animal

