from daos.daoAbstrato import DAO
from entidade.cachorro import Cachorro

#cada entidade terá uma classe dessa, implementação bem simples.
class CachorroDAO(DAO):
    def __init__(self):
        super().__init__('cachorros.pkl')

    def add(self, cachorro: Cachorro):
        if((cachorro is not None) and isinstance(cachorro, Cachorro) and isinstance(cachorro.num_chip, int)):
            super().add(cachorro.num_chip, cachorro)

    def update(self, cachorro: Cachorro, chip: int):
        if((cachorro is not None) and isinstance(cachorro, Cachorro) and isinstance(chip, int)):
            super().update(chip, cachorro)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)