class ControladorPrincipal:
    def __init__(self):
        from controle.controladorDoador import ControladorDoador
        self.__controlador_doador = ControladorDoador(self)

        from controle.controladorAdotante import ControladorAdotante
        self.__controlador_adotante = ControladorAdotante(self)

        from controle.controladorDoacao import ControladorDoacao
        self.__controlador_doacao = ControladorDoacao(self)

        from controle.controladorAdocao import ControladorAdocao
        self.__controlador_adocao = ControladorAdocao(self)

        from controle.controladorCachorro import ControladorCachorro
        self.__controlador_cachorro = ControladorCachorro(self)

        from controle.controladorGato import ControladorGato
        self.__controlador_gato = ControladorGato(self)

        from controle.controladorAnimal import ControladorAnimal
        self.__controlador_animal = ControladorAnimal(self)

        from controle.controladorVacinacao import ControladorVacinacao
        self.__controlador_vacinacao = ControladorVacinacao(self)

        from limite.telaPrincipal import TelaPrincipal
        self.__tela_principal = TelaPrincipal()

    @property
    def controladorDoador(self):
        return self.__controlador_doador

    @property
    def controladorAdotante(self):
        return self.__controlador_adotante

    @property
    def controladorDoacao(self):
        return self.__controlador_doacao

    @property
    def controladorAdocao(self):
        return self.__controlador_adocao

    @property
    def controladorAnimal(self):
        return self.__controlador_animal

    @property
    def controladorCachorro(self):
        return self.__controlador_cachorro

    @property
    def controladorGato(self):
        return self.__controlador_gato

    @property
    def controladorVacinacao(self):
        return self.__controlador_vacinacao

    def cadastrar_doador(self):
        # Chama o controlador de doador
        self.__controlador_doador.abre_tela()

    def cadastrar_adotante(self):
        # Chama o controlador de adotante
        self.__controlador_adotante.abre_tela()

    def registrar_doacao(self):
        self.__controlador_doacao.abrir_tela()

    def registrar_adocao(self):
        self.__controlador_adocao.abrir_tela()

    def visualizar_animal(self):
        self.__controlador_animal.abrir_tela()

    def visualizar_cachorro(self):
        self.__controlador_cachorro.abrir_tela()

    def visualizar_gato(self):
        self.__controlador_gato.abrir_tela()

    def visualizar_historico(self):
        self.__controlador_vacinacao.abre_tela()

    def iniciar_controlador(self):
        self.abre_tela()

    def encerrar_sistema(self):
        self.__tela_principal.mensagem("Sistema Finalizado.")
        exit(0)

    def animal_por_chip(self, id):
        cachorro = self.__controlador_cachorro.cachorro_por_chip(id)
        if cachorro != 'Cachorro nao se encontra no sistema.':
            return cachorro
        gato = self.__controlador_gato.gato_por_chip(id)
        if gato != 'Gato nao se encontra no sistema.':
            return gato
        return 'Animal não se encontra no sistema.'

    def abre_tela(self):
        # Ir adicionando mais opcoes a media que os controladores/telas forem sendo adicionados
        lista_opcoes = {0: self.encerrar_sistema,
                        1: self.cadastrar_doador,
                        2: self.cadastrar_adotante,
                        3: self.registrar_doacao,
                        4: self.registrar_adocao,
                        5: self.visualizar_animal,
                        6: self.visualizar_historico}

        while True:
            opcao_escolhida = self.__tela_principal.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
