class ControladorPrincipal:
    def __init__(self):
        from controle.controladorDoador import ControladorDoador
        self.__controladorDoador = ControladorDoador(self)

        from controle.controladorAdotante import  ControladorAdotante
        self.__controladorAdotante = ControladorAdotante(self)

        from controle.controladorDoacao import ControladorDoacao
        self.__controladorDoacao = ControladorDoacao(self)

        from controle.controladorAdocao import ControladorAdocao
        self.__controladorAdocao = ControladorAdocao(self)

        from controle.controladorAnimal import ControladorAnimal
        self.__controladorAnimal = ControladorAnimal(self)

        from controle.controladorCachorro import ControladorCachorro
        self.__controladorCachorro = ControladorCachorro(self)

        from controle.controladorGato import ControladorGato
        self.__controladorGato = ControladorGato(self)

        from limite.telaPrincipal import TelaPrincipal
        self.__tela_principal = TelaPrincipal()

    @property
    def controladorDoador(self):
        return self.__controladorDoador
    
    @property
    def controladorAdotante(self):
        return self.__controladorAdotante
    
    @property
    def controladorDoacao(self):
        return self.__controladorDoacao
    
    @property
    def controladorAdocao(self):
        return self.__controladorAdocao
    
    @property
    def controladorAnimal(self):
        return self.__controladorAnimal

    @property
    def controladorCachorro(self):
        return self.__controladorCachorro

    @property
    def controladorGato(self):
        return self.__controladorGato

    def cadastrar_doador(self):
        #Chama o controlador de doador
        self.__controladorDoador.abre_tela()

    def cadastrar_adotante(self):
        #Chama o controlador de adotante
        self.__controladorAdotante.abre_tela()

    def registrar_doacao(self):
        self.__controladorDoacao.abrir_tela()

    def registrar_adocao(self):
        self.__controladorAdocao.abrir_tela()

    def visualizar_animal(self):
        self.__controladorAnimal.abrir_tela()

    def visualizar_cachorro(self):
        self.__controladorCachorro.abrir_tela()

    def visualizar_gato(self):
        self.__controladorGato.abrir_tela()

    def iniciar_controlador(self):
        self.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def animal_por_chip(self, id):
        cachorro = self.__controladorCachorro.cachorro_por_chip(id)
        if cachorro != 'Cachorro nao se encontra no sistema.':
            return cachorro
        gato = self.__controladorGato.gato_por_chip(id)
        if gato != 'Gato nao se encontra no sistema.':
            return gato
        return 'Animal não se encontra no sistema.'
        

    def abre_tela(self):
        #Ir adicionando mais opcoes a media que os controladores/telas forem sendo adicionados
        lista_opcoes = {0: self.encerrar_sistema,
                        1: self.cadastrar_doador,
                        2: self.cadastrar_adotante,
                        3: self.registrar_doacao,
                        4: self.registrar_adocao,
                        5: self.visualizar_animal}

        while True:
            opcao_escolhida = self.__tela_principal.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
