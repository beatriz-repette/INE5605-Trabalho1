from entidades.pessoa import Pessoa
from datetime import date


class Doador(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(cpf, nome, data_nascimento, endereco)
