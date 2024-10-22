from abc import ABC, abstractmethod


class ControladorAbstrato(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.__tela = None

    @abstractmethod
    def incluir(self):
        pass

    @abstractmethod
    def alterar(self):
        pass

    @abstractmethod
    def excluir(self):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def finalizar(self):
        pass

    def abre_tela(self):
        switch = {
            0: self.finalizar,
            1: self.incluir,
            2: self.alterar,
            3: self.excluir,
            4: self.listar,
            }
        while True:
            opcao = self.__tela.mostrar_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()