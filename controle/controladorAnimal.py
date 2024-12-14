class ControladorAnimal():
    def __init__(self, contPrincipal) -> None:
        from controle.controladorPrincipal import ControladorPrincipal
        self.__controladorPrincipal = contPrincipal

        from controle.controladorCachorro import ControladorCachorro

        self.__controlador_cachorro = self.__controladorPrincipal.controladorCachorro
        from controle.controladorGato import ControladorGato
        self.__controlador_gato = self.__controladorPrincipal.controladorGato

        from limite.telaAnimal import TelaAnimal
        self.__telaAnimal = TelaAnimal()

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

    def animal_por_chip(self, id):
        cachorro = self.__controlador_cachorro.cachorro_por_chip(id)
        if cachorro != 'Cachorro nao se encontra no sistema.':
            return cachorro
        gato = self.__controlador_gato.gato_por_chip(id)
        if gato != 'Gato nao se encontra no sistema.':
            return gato
        return 'Animal não se encontra no sistema.'

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
