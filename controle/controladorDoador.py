from limite.telaDoador import TelaDoador
from entidade.doador import Doador
from exception.retornarException import RetornarException
from exception.erroCadastroException import ErroCadastroException


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
        try:
            if dados_doador == 0:
                self.__telaDoador.mensagem_operacao_cancelada()
                raise RetornarException

            for doa in self.__doadores:
                if doa.cpf == dados_doador["cpf"]:
                    self.__telaDoador.mensagem_erro_cadastro()
                    raise ErroCadastroException
            doador = Doador(dados_doador["cpf"], dados_doador["nome"], dados_doador["data_nascimento"], dados_doador["endereco"])
            self.__doadores.append(doador)
            self.__telaDoador.mensagem_operacao_concluida()
        except:
            pass

    def alterar_doador(self):
        cpf_doador = self.__telaDoador.seleciona_doador()  # Seleciona retorna o cpf para fazer buscas em listas
        if cpf_doador == '0':
            self.__telaDoador.mensagem_operacao_cancelada()
            raise RetornarException
        
        doador = self.doador_por_cpf(cpf_doador)

        if doador is not None:
            try:
                novos_dados_doador = self.__telaDoador.pega_dados_alterados_doador()

                if novos_dados_doador == 0:
                    self.__telaDoador.mensagem_operacao_cancelada()
                    raise RetornarException

                if novos_dados_doador["cpf"] != '*':
                    # Verifica se ja existe um cadastro com o novo cpf informado
                    if self.doador_por_cpf(novos_dados_doador['cpf']) is not None:
                        self.__telaDoador.mensagem_erro_cadastro()
                        raise ErroCadastroException
                    doador.cpf = novos_dados_doador["cpf"]

                if novos_dados_doador["nome"] != '*':
                    doador.nome = novos_dados_doador["nome"]

                if novos_dados_doador["data_nascimento"] != '*':
                    doador.data_nascimento = novos_dados_doador["data_nascimento"]

                if novos_dados_doador["endereco"] != '*':
                    doador.endereco = novos_dados_doador["endereco"]

                self.__telaDoador.mensagem_operacao_concluida()

            except ErroCadastroException or RetornarException:
                pass
        else:
            self.__telaDoador.mensagem_doador_nao_existente()

    def excluir_doador(self):
        cpf_doador = self.__telaDoador.seleciona_doador() #Seleciona retorna o cpf para fazer buscas em listas
        doador = self.doador_por_cpf(cpf_doador)

        if doador is not None:
            self.__doadores.remove(doador)
            self.__telaDoador.mensagem_operacao_concluida()
        else:
            self.__telaDoador.mensagem_doador_nao_existente()

    @property
    def doadores(self):
        return self.__doadores

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

    def listar_doadores(self):
        if self.__doadores == []:
            self.__telaDoador.mensagem_non_existent()
        else:
            for doador in self.__doadores:
                self.__telaDoador.mostra_doador({"nome": doador.nome, "endereco": doador.endereco, "cpf": doador.cpf, "data_nascimento": doador.data_nascimento})

    def abre_tela(self): #anteriormente funcao se chamava "iniciar"
        lista_opcoes = {1 : self.incluir_doador, 2 : self.alterar_doador, 3 : self.listar_doadores, 4 : self.excluir_doador, 0 : self.finalizar}

        while True: #no exemplo ta como 'continua'
            funcao_escolhida = lista_opcoes[self.__telaDoador.tela_opcoes()]
            funcao_escolhida()
