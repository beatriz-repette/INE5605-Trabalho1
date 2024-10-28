from entidade.cachorro import Cachorro

class ControladorCachorro():
    from controle.controladorPrincipal import ControladorPrincipal
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__cachorros = []

    def incluir_cachorro(self, dados):
        dog = Cachorro(dados['chip'], dados['nome'], dados['raca'], dados['tamanho'], dados['vacinas'])
        self.__cachorros.append(dog)
        return dog
    
    def cachorro_por_chip(self, id):
        for cachorro in self.__cachorros:
            if cachorro.chip_id == id:
                return cachorro
        return 'Cachorro nao se encontra no sistema.'

    @property
    def cachorros(self):
        return self.__cachorros
