from daos.daoAbstrato import DAO
from entidade.doacao import Doacao

class DoacaoDAO(DAO):
    def __init__(self):
        super().__init__('doacoes.pkl')
        self.__cache = []

    def add(self, doacao: Doacao, key: int):
        if((doacao is not None) and isinstance(doacao, Doacao) and isinstance(key, int)):
            super().add(key, doacao)

    def update(self, doacao: Doacao, key: int):
        if((doacao is not None) and isinstance(doacao, Doacao) and isinstance(key, int)):
            super().update(key, doacao) #key eh o len

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        # FAZER TODAS AS KEYS POSTERIORES SERES KEY-1
        if(isinstance(key, int)):
            while key < len(super().get_all()):
                super().update(key, super().get(key+1))
                key += 1
            super().remove(key)
