from daos.daoAbstrato import DAO
from entidade.doador import Doador

class DoadorDAO(DAO):
    def __init__(self):
        super().__init__('doadores.pkl')

    def add(self, cpf, doador: Doador):
        if((doador is not None) and isinstance(doador, Doador) and isinstance(doador.cpf, str)):
            super().add(cpf, doador)

    def update(self, cpf: str, doador: Doador):
        if((doador is not None) and isinstance(doador, Doador) and isinstance(cpf, str)):
            super().update(cpf, doador)

    def get(self, key:int):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, str)):
            return super().remove(key)