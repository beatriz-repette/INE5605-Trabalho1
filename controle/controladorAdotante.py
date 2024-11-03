from limite.telaAdotante import TelaAdotante
from entidade.adotante import Adotante
from entidade.habitacao import Habitacao
from exception.retornarException import RetornarException
from exception.erroCadastroException import ErroCadastroException

class ControladorAdotante:
    def __init__(self, controladorPrincipal):
        self.__adotantes = []
        self.__telaAdotante = TelaAdotante()
        self.__controladorPrincipal = controladorPrincipal

    def adotante_por_cpf(self, cpf):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None

    def incluir_adotante(self):
        try:
            dados_adotante = self.__telaAdotante.pega_dados_adotante()
            if dados_adotante == 0:
                self.__telaAdotante.mensagem_operacao_cancelada()
                raise RetornarException
            for doa in self.__adotantes:
                if doa.cpf == dados_adotante["cpf"]:
                    self.__telaAdotante.mensagem_erro_cadastro()
                    raise ErroCadastroException
            adotante = Adotante(dados_adotante["cpf"], dados_adotante["nome"], dados_adotante["data_nascimento"],
                                dados_adotante["endereco"], Habitacao(dados_adotante["tipo_habitacao"]), dados_adotante["possui_animal"])
            self.__adotantes.append(adotante)
        except RetornarException or ErroCadastroException:
            pass

    def alterar_adotante(self):
        cpf_adotante = self.__telaAdotante.seleciona_adotante()  # Seleciona retorna o cpf para fazer buscas em listas
        adotante = self.adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            try:
                novos_dados_adotante = self.__telaAdotante.pega_dados_adotante()

                if novos_dados_adotante == 0:
                    self.__telaAdotante.mensagem_operacao_cancelada()
                    raise RetornarException

                # Verifica se ja existe um cadastro com o novo cpf informado
                for doa in self.__adotantes:
                    if doa.cpf == novos_dados_adotante["cpf"]:
                        self.__telaAdotante.mensagem_erro_cadastro()
                        raise ErroCadastroException

                adotante.cpf = novos_dados_adotante["cpf"]
                adotante.nome = novos_dados_adotante["nome"]
                adotante.data_nascimento = novos_dados_adotante["data_nascimento"]
                adotante.endereco = novos_dados_adotante["endereco"]
                self.__telaAdotante.mensagem_operacao_concluida()

            except ErroCadastroException or RetornarException:
                pass
        else:
            self.__telaAdotante.mensagem_adotante_nao_existente()

    def listar_adotantes(self):
        if self.__adotantes == []:
            self.__telaAdotante.mensagem_non_existent()
        else:
            for adotante in self.__adotantes:
                self.__telaAdotante.mostra_adotante({"nome": adotante.nome,
                                                    "endereco": adotante.endereco,
                                                    "cpf": adotante.cpf,
                                                    "data_nascimento": adotante.data_nascimento,
                                                    "tipo_habitacao": adotante.tipo_habitacao._name_.replace('_'," "),
                                                    "possui_animal": adotante.possui_animal})

    def excluir_adotante(self):
        cpf_adotante = self.__telaAdotante.seleciona_adotante()  # Seleciona retorna o cpf para fazer buscas em listas
        adotante = self.adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            self.__adotantes.remove(adotante)
            self.__telaAdotante.mensagem_operacao_concluida()
        else:
            self.__telaAdotante.mensagem_adotante_nao_existente()

    @property
    def adotantes(self):
        return self.__adotantes

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

    def abre_tela(self):  # anteriormente funcao se chamava "iniciar"
        lista_opcoes = {1: self.incluir_adotante, 2: self.alterar_adotante, 3: self.listar_adotantes, 4: self.excluir_adotante,
                        0: self.finalizar}

        while True:  # no exemplo ta como 'continua'
            funcao_escolhida = lista_opcoes[self.__telaAdotante.tela_opcoes()]
            funcao_escolhida()
