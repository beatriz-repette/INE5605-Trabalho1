from entidade.cachorro import Cachorro

class ControladorCachorro():
    def __init__(self):
        from controle.controladorPrincipal import ControladorPrincipal
        self.__controladorPrincipal = ControladorPrincipal
        self.__cachorros = []

    def incluir_cachorro(self, dados):
        self.__cachorros.append(Cachorro(dados['chip'], dados['nome'], dados['raca'], dados['tamanho'], dados['vacinas']))
