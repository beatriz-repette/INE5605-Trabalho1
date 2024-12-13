from daos.daoAbstrato import DAO
from entidade.gato import Gato

#cada entidade terá uma classe dessa, implementação bem simples.
class GatoDAO(DAO):
    def __init__(self):
        super().__init__('gatos.pkl')

    def add(self, gato: Gato):
        if((gato is not None) and isinstance(gato, Gato) and isinstance(gato.num_chip, int)):
            super().add(gato.num_chip, gato)

    def update(self, gato: Gato, chip: int):
        if((gato is not None) and isinstance(gato, Gato) and isinstance(chip, int)):
            super().update(chip, gato)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)