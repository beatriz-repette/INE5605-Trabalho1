from limite.telaDoador import TelaDoador
from entidade.doador import Doador


class ControladorDoador:
    def __init__(self, controladorPrincipal):
        self.__doadores = []
        self.__telaDoador = TelaDoador()
        self.__controladorPrincipal = controladorPrincipal

    def doador_por_cpf(self, cpf):
        for doador in self.__doadores:
            if doador.cpf == cpf:
                return doador
        return None

    def incluir_doador(self):
        dados_doador = self.__telaDoador.pega_dados_doador()
        for doa in self.__doadores:
            if doa.cpf == dados_doador["cpf"]:
                return
        doador = Doador(dados_doador["cpf"], dados_doador["nome"], dados_doador["data_nascimento"], dados_doador["endereco"])
        self.__doadores.append(doador)

    def alterar_doador(self):
        cpf_doador = self.__telaDoador.seleciona_doador() #Seleciona retorna o cpf para fazer buscas em listas
        doador = self.doador_por_cpf(cpf_doador)

        if doador is not None:
            novos_dados_doador = self.__telaDoador.pega_dados_doador()
            doador.cpf = novos_dados_doador["cpf"]
            doador.nome = novos_dados_doador["nome"]
            doador.data_nascimento = novos_dados_doador["data_nascimento"]
            doador.endereco = novos_dados_doador["endereco"]
        #Talvez exibir uma mensagem caso nn exista esse amigo? Ou da pra, na tela, so aceitar cpf validos

    def excluir_doador(self):
        cpf_doador = self.__telaDoador.seleciona_doador() #Seleciona retorna o cpf para fazer buscas em listas
        doador = self.doador_por_cpf(cpf_doador)

        if doador is not None:
            self.__doadores.remove(doador)
        #Opcional: adicionar mensagem caso doador a ser deletado ja nao exista

    @property
    def doadores(self):
        return self.__doadores

    def finalizar(self): #Mudar o nome para 'retornar'?
        self.__controladorPrincipal.abre_tela()

    def listar_doadores(self):
        for doador in self.__doadores:
            self.__telaDoador.mostra_doador({"nome": doador.nome, "endereco": doador.endereco, "cpf": doador.cpf, "data_nascimento": doador.data_nascimento})

    def abre_tela(self): #anteriormente funcao se chamava "iniciar"
        lista_opcoes = {1 : self.incluir_doador, 2 : self.alterar_doador, 3 : self.listar_doadores, 4 : self.excluir_doador, 0 : self.finalizar}

        while True: #no exemplo ta como 'continua'
            funcao_escolhida = lista_opcoes[self.__telaDoador.tela_opcoes()]
            funcao_escolhida()
  
