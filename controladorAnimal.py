class ControladorAnimal():
    def __init__(self, contPrincipal) -> None:
        from controle.controladorPrincipal import ControladorPrincipal
        self.__controladorPrincipal = contPrincipal

        from limite.telaAnimal import TelaAnimal
        self.__telaAnimal = TelaAnimal()

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

    def abrir_tela(self):
        while True:
            switch = {
                0: self.finalizar,
                1: self.__controladorPrincipal.visualizar_gato,
                2: self.__controladorPrincipal.visualizar_cachorro
            }
            opcao = self.__telaAnimal.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
            break
