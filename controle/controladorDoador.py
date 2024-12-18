from limite.telaDoador import TelaDoador
from entidade.doador import Doador
from exception.retornarException import RetornarException
from exception.erroCadastroException import ErroCadastroException
from daos.daoDoador import DoadorDAO


class ControladorDoador:
    def __init__(self, controladorPrincipal):
        self.__doadores_DAO = DoadorDAO()
        self.__tela_doador = TelaDoador()
        self.__controlador_principal = controladorPrincipal

    def doador_por_cpf(self, cpf):
        for doador in self.__doadores_DAO.get_all():
            if doador.cpf == cpf:
                return doador
        return None

    def incluir_doador(self):
        dados_doador = self.__tela_doador.pega_dados_doador()
        try:
            if dados_doador == 0:
                self.__tela_doador.mensagem_operacao_cancelada()
                raise RetornarException

            for doa in self.__doadores_DAO.get_all():
                if doa.cpf == dados_doador["cpf"]:
                    self.__tela_doador.mensagem("Erro ao cadastrar doador, CPF inserido ja cadastrado")
                    raise ErroCadastroException
            doador = Doador(dados_doador["cpf"], dados_doador["nome"], dados_doador["data_nascimento"],
                            dados_doador["endereco"])
            self.__doadores_DAO.add(dados_doador["cpf"], doador)
            self.__tela_doador.mensagem_operacao_concluida()
        except:
            pass

    def alterar_doador(self):
        cpf_doador = self.__tela_doador.seleciona_doador()  # Seleciona retorna o cpf para fazer buscas em listas
        if cpf_doador == '0':
            self.__tela_doador.mensagem_operacao_cancelada()
            raise RetornarException

        doador = self.doador_por_cpf(cpf_doador)

        if doador is not None:
            try:
                novos_dados_doador = self.__tela_doador.pega_dados_alterados_doador()

                if novos_dados_doador == 0:
                    self.__tela_doador.mensagem_operacao_cancelada()
                else:
                    if novos_dados_doador["cpf"] != '':
                        # Verifica se ja existe um cadastro com o novo cpf informado
                        if self.doador_por_cpf(novos_dados_doador['cpf']) is not None:
                            self.__tela_doador.mensagem("Erro ao cadastrar doador, CPF inserido ja cadastrado")
                            raise ErroCadastroException
                        doador.cpf = novos_dados_doador["cpf"]

                    if novos_dados_doador["nome"] != '':
                        doador.nome = novos_dados_doador["nome"]

                    if novos_dados_doador["data_nascimento"] != '':
                        doador.data_nascimento = novos_dados_doador["data_nascimento"]

                    if novos_dados_doador["endereco"] != '':
                        doador.endereco = novos_dados_doador["endereco"]

                    self.__doadores_DAO.update(cpf_doador, doador)
                    self.__tela_doador.mensagem_operacao_concluida()

            except ErroCadastroException or RetornarException:
                pass
        else:
            self.__tela_doador.mensagem("Nao existe nenhum cadastro de doador com esse CPF")

    def excluir_doador(self):
        cpf_doador = self.__tela_doador.seleciona_doador()  # Seleciona retorna o cpf para fazer buscas em listas
        doador = self.doador_por_cpf(cpf_doador)

        if doador is not None:
            self.__doadores_DAO.remove(cpf_doador)
            self.__tela_doador.mensagem_operacao_concluida()
        else:
            self.__tela_doador.mensagem("Nao existe nenhum cadastro de doador com esse CPF")

    @property
    def doadores(self):
        return self.__doadores_DAO.get_all()

    def finalizar(self):
        self.__controlador_principal.abre_tela()

    def listar_doadores(self):
        if self.doadores == []:
            self.__tela_doador.mensagem("Nao existem doadores no sistema.")
        else:
            dados_tabela = [
                [
                    doador.nome,
                    doador.endereco,
                    doador.cpf,
                    doador.data_nascimento.strftime('%d/%m/%Y')
                ]
                for doador in self.__doadores_DAO.get_all()  # roda a lista
            ]

            # Envia os dados para a View
            self.__tela_doador.mostra_doador(dados_tabela)

    def abre_tela(self):  # anteriormente funcao se chamava "iniciar"
        lista_opcoes = {1: self.incluir_doador, 2: self.alterar_doador, 3: self.listar_doadores, 4: self.excluir_doador,
                        0: self.finalizar}

        while True:  # no exemplo ta como 'continua'
            funcao_escolhida = lista_opcoes[self.__tela_doador.tela_opcoes()]
            funcao_escolhida()
