from entidades.animal import Animal


class Gato(Animal):
    def __init__(self, num_chip: int, nome: str, raca: str):
        super().__init__(num_chip, nome, raca)