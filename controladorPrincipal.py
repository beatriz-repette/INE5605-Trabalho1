from controladorDoador import ControladorDoador
from telaPrincipal import TelaPrincipal


class ControladorPrincipal:
    def __init__(self):
        self.__controladorDoador = ControladorDoador(self)

    @property
    def controladorDoador(self):
        return self.__controladorDoador
    
    def cadastra_doador(self):
        #Chama o controlador de doador
        self.__controladorDoador.abre_tela()

    def iniciar_controlador(self, controlador):
        pass

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_doador, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
