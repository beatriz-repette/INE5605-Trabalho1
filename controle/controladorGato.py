from entidade.gato import Gato
from controle.controladorPrincipal import ControladorPrincipal

class ControladorGato():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__gatos = []

    def incluir_gato(self, dados):
        cat = Gato(dados['chip'], dados['nome'], dados['raca'], dados['vacinas'])
        self.__gatos.append(cat)
        return cat
    
    def gato_por_chip(self, id):
        for gato in self.__gatos:
            if gato.num_chip == id:
                return gato
        return 'Gato nao se encontra no sistema.'

    @property
    def gatos(self):
        return self.__gatos