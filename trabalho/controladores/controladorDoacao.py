from entidades.doacao import Doacao
from telas.telaDoacao import TelaDoacao


class ControladorDoacao():
    def __init__(self) -> None:
        self.__tela = TelaDoacao(self)
        self.__doacoes = []

    def incluir_doacao(self):
        pass

    def listar_doacoes(self):
        return self.__doacoes

    def finalizar(self):
        pass

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.incluir_doacao,
            2: self.listar_doacoes,
            }
        while True:
            opcao = self.__tela.mostrar_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()


