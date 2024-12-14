from limite.telaAdotante import TelaAdotante
from entidade.adotante import Adotante
from entidade.habitacao import Habitacao
from exception.retornarException import RetornarException
from exception.erroCadastroException import ErroCadastroException
from daos.daoAdotante import AdotanteDAO


class ControladorAdotante:
    def __init__(self, controladorPrincipal):
        self.__adotantes_DAO = AdotanteDAO()
        self.__tela_adotante = TelaAdotante()
        self.__controlador_principal = controladorPrincipal

    @property
    def adotantes(self):
        return self.__adotantes_DAO.get_all()

    def adotante_por_cpf(self, cpf):
        for adotante in self.__adotantes_DAO.get_all():
            if adotante.cpf == cpf:
                return adotante
        return None

    def incluir_adotante(self):
        try:
            dados_adotante = self.__tela_adotante.pega_dados_adotante()
            if dados_adotante == 0:
                self.__tela_adotante.mensagem_operacao_cancelada()
                raise RetornarException
            for doa in self.adotantes:
                if doa.cpf == dados_adotante["cpf"]:
                    self.__tela_adotante.mensagem("Erro ao cadastrar adotante, CPF inserido ja cadastrado.")
                    raise ErroCadastroException
            adotante = Adotante(dados_adotante["cpf"], dados_adotante["nome"], dados_adotante["data_nascimento"],
                                dados_adotante["endereco"], Habitacao(dados_adotante["tipo_habitacao"]),
                                dados_adotante["possui_animal"])
            self.__adotantes_DAO.add(dados_adotante["cpf"], adotante)

            self.__tela_adotante.mensagem_operacao_concluida()
        except (RetornarException, ErroCadastroException, KeyError):
            pass

    def alterar_adotante(self):
        cpf_adotante = self.__tela_adotante.seleciona_adotante()  # Seleciona retorna o cpf para fazer buscas em listas
        if cpf_adotante == '0':
            self.__tela_adotante.mensagem_operacao_cancelada()
            raise RetornarException

        adotante = self.adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            try:
                self.__tela_adotante.mensagem("A seguir, insira os novos dados do adotante.")
                novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()

                if novos_dados_adotante == 0:
                    self.__tela_adotante.mensagem_operacao_cancelada()
                    raise RetornarException

                if novos_dados_adotante["cpf"] != '*':
                    # Verifica se ja existe um cadastro com o novo cpf informado
                    if self.adotante_por_cpf(novos_dados_adotante['cpf']) is not None:
                        self.__tela_adotante.mensagem("Erro ao cadastrar adotante, CPF inserido ja cadastrado.")
                        raise ErroCadastroException
                    adotante.cpf = novos_dados_adotante["cpf"]

                if novos_dados_adotante["nome"] != '*':
                    adotante.nome = novos_dados_adotante["nome"]

                if novos_dados_adotante["data_nascimento"] != '*':
                    adotante.data_nascimento = novos_dados_adotante["data_nascimento"]

                if novos_dados_adotante["endereco"] != '*':
                    adotante.endereco = novos_dados_adotante["endereco"]

                if novos_dados_adotante["tipo_habitacao"] != '*':
                    adotante.tipo_habitacao = novos_dados_adotante["tipo_habitacao"]

                if novos_dados_adotante["possui_animal"] != '*':
                    adotante.possui_animal = novos_dados_adotante['possui_animal']

                self.__adotantes_DAO.update(adotante.cpf, adotante)
                self.__tela_adotante.mensagem_operacao_concluida()

            except ErroCadastroException or RetornarException:
                pass
        else:
            self.__tela_adotante.mensagem("Nao existe nenhum cadastro de adotante com esse CPF.")

    def listar_adotantes(self):
        if self.adotantes == []:
            self.__tela_adotante.mensagem("Nao existem adotantes no sistema.")
        else:
            dados_tabela = [
                [
                    adotante.nome,
                    adotante.endereco,
                    adotante.cpf,
                    adotante.data_nascimento.strftime('%d/%m/%Y'),
                    adotante.tipo_habitacao._name_.replace('_', ' '),
                    "Sim" if adotante.possui_animal else "Não"
                ]
                for adotante in self.__adotantes_DAO.get_all()
            ]

            # Envia os dados para a View
            self.__tela_adotante.mostra_adotante(dados_tabela)

    def excluir_adotante(self):
        cpf_adotante = self.__tela_adotante.seleciona_adotante()  # Seleciona retorna o cpf para fazer buscas em listas
        adotante = self.adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            self.__adotantes_DAO.remove(cpf_adotante)
            self.__tela_adotante.mensagem_operacao_concluida()
        else:
            self.__tela_adotante.mensagem("Nao existe nenhum cadastro de adotante com esse CPF.")

    def finalizar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):  # anteriormente funcao se chamava "iniciar"
        lista_opcoes = {1: self.incluir_adotante, 2: self.alterar_adotante, 3: self.listar_adotantes,
                        4: self.excluir_adotante,
                        0: self.finalizar}

        while True:  # no exemplo ta como 'continua'
            funcao_escolhida = lista_opcoes[self.__tela_adotante.tela_opcoes()]
            funcao_escolhida()
