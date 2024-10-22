from entidade.gato import Gato

class ControladorGato():
    def __init__(self):
        from controle.controladorPrincipal import ControladorPrincipal
        self.__controladorPrincipal = ControladorPrincipal
        self.__gatos = []

    def incluir_gato(self, dados):
        self.__gatos.append(Gato(dados['chip'], dados['nome'], dados['raca'], dados['vacinas']))
