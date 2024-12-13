from daos.daoAbstrato import DAO
from entidade.vacinacao import Vacinacao

#cada entidade terá uma classe dessa, implementação bem simples.
class VacinacaoDAO(DAO):
    def __init__(self):
        super().__init__('vacinacoes.pkl')

    def add(self, vacinacao: Vacinacao, key: int):
        if((vacinacao is not None) and isinstance(vacinacao, Vacinacao) and isinstance(key, int)):
            super().add(key, vacinacao)

    def update(self, vacinacao: Vacinacao, key: int):
        if((vacinacao is not None) and isinstance(vacinacao, Vacinacao) and isinstance(key, int)):
            super().update(key, vacinacao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)