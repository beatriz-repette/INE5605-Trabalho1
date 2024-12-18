from entidade.animal import Animal


class Cachorro(Animal):
    def __init__(self, num_chip: int, nome: str, raca: str, tamanho: str, vacinas = []):
        super().__init__(num_chip, nome, raca, vacinas)
        self.__tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tam: str):
        self.__tamanho = tam
