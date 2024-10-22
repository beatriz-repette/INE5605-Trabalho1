from controle.controladorCachorro import ControladorCachorro
from controle.controladorDoador import ControladorDoador
from limite.telaPrincipal import TelaPrincipal
from controle.controladorDoacao import ControladorDoacao
from controle.controladorGato import ControladorGato
from controle.controladorCachorro import ControladorCachorro


class ControladorPrincipal:
    def __init__(self):
        self.__controladorDoador = ControladorDoador
        self.__controladorDoacao = ControladorDoacao
        self.__controladorCachorro = ControladorCachorro()
        self.__controladorGato = ControladorGato()
        self.__tela_sistema = TelaPrincipal()

    @property
    def controladorDoador(self):
        return self.__controladorDoador
    
    def cadastrar_doador(self):
        #Chama o controlador de doador
        self.__controladorDoador().abrir_tela()

    def cadastrar_doacao(self):
        self.__controladorDoacao().abrir_tela()

    def iniciar_controlador(self, controlador):
        pass

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {0: self.encerra_sistema, 1: self.cadastrar_doador, 2: self.cadastrar_doacao}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    @property
    def controladorCachorro(self):
        return self.__controladorCachorro

    @property
    def controladorGato(self):
        return self.__controladorGato
