from controle.controladorDoador import ControladorDoador
from limite.telaPrincipal import TelaPrincipal


class ControladorPrincipal:
    def __init__(self):
        self.__controladorDoador = ControladorDoador(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def controladorDoador(self):
        return self.__controladorDoador
    
    def cadastra_doador(self):
        #Chama o controlador de doador
        self.__controladorDoador.abre_tela()

    def iniciar_controlador(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        #Ir adicionando mais opcoes a media que os controladores/telas forem sendo adicionados
        lista_opcoes = {1: self.cadastra_doador, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_principal.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
