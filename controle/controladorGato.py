from entidade.gato import Gato
from controle.controladorPrincipal import ControladorPrincipal
from limite.telaGato import TelaGato

class ControladorGato():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__telaGato = TelaGato()
        self.__gatos = []

    def listar_gatos(self):
        if self.__gatos == []:
            print('Nao existem gatos no sistema.')
        else:
            for a in self.__gatos:
                self.__telaGato.mostrar_gato({
                    'animal': a.nome,
                    'chip': a.num_chip,
                    'raca': a.raca,
                    'adotado': self.__controladorPrincipal.controladorAdocao.animal_foi_adotado(a.num_chip)
                    })

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

    def finalizar(self):
        self.__controladorPrincipal.controladorAnimal.abrir_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.listar_gatos,
            }
        while True:
            opcao = self.__telaGato.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()