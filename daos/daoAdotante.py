from daos.daoAbstrato import DAO
from entidade.adotante import Adotante

class AdotanteDAO(DAO):
    def __init__(self):
        super().__init__('adotantes.pkl')

    def add(self, cpf, adotante: Adotante):
        if((adotante is not None) and isinstance(adotante, Adotante) and isinstance(cpf, str)):
            super().add(adotante.cpf, adotante)

    def update(self, cpf: str, adotante: Adotante):
        if((adotante is not None) and isinstance(adotante, Adotante) and isinstance(cpf, str)):
            super().update(adotante.cpf, adotante)

    def get(self, key:int):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, str)):
            return super().remove(key)