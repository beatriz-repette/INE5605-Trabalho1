from daos.daoAbstrato import DAO
from entidade.adocao import Adocao

class AdocaoDAO(DAO):
    def __init__(self):
        super().__init__('adocoes.pkl')
        self.__cache = []

    def add(self, adocao: Adocao):
        if((adocao is not None) and isinstance(adocao, Adocao)):
            super().add(adocao)

    def update(self, adocao: Adocao, key: int):
        if((adocao is not None) and isinstance(adocao, Adocao) and isinstance(key, int)):
            super().update(key, adocao) #key eh o len

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)