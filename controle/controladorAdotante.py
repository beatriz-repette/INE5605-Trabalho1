from limite.telaAdotante import TelaAdotante
from entidade.adotante import Adotante


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
        dados_adotante = self.__telaAdotante.pega_dados_adotante()
        for doa in self.__adotantes:
            if doa.cpf == dados_adotante["cpf"]:
                return
        adotante = Adotante(dados_adotante["cpf"], dados_adotante["nome"], dados_adotante["data_nascimento"],
                        dados_adotante["endereco"], dados_adotante["tipo_habitacao"], dados_adotante["possui_animal"])
        self.__adotantes.append(adotante)

    def alterar_adotante(self):
        cpf_adotante = self.__telaAdotante.seleciona_adotante()  # Seleciona retorna o cpf para fazer buscas em listas
        adotante = self.adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            novos_dados_adotante = self.__telaAdotante.pega_dados_adotante()
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.nome = novos_dados_adotante["nome"]
            adotante.data_nascimento = novos_dados_adotante["data_nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
        # Talvez exibir uma mensagem caso nn exista esse amigo? Ou da pra, na tela, so aceitar cpf validos

    def excluir_adotante(self):
        cpf_adotante = self.__telaAdotante.seleciona_adotante()  # Seleciona retorna o cpf para fazer buscas em listas
        adotante = self.adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            self.__adotantes.remove(adotante)
        # Opcional: adicionar mensagem caso doador a ser deletado ja nao exista

    @property
    def adotantes(self):
        return self.__adotantes

    def finalizar(self):  # Mudar o nome para 'retornar'?
        self.__controladorPrincipal.abre_tela()

    def listar_adotantes(self):
        for adotante in self.__adotantes:
            self.__telaAdotante.mostra_adotante({"nome": adotante.nome, "endereco": adotante.endereco, "cpf": adotante.cpf,
                                             "data_nascimento": adotante.data_nascimento})

    def abre_tela(self):  # anteriormente funcao se chamava "iniciar"
        lista_opcoes = {1: self.incluir_adotante, 2: self.alterar_adotante, 3: self.listar_adotantes, 4: self.excluir_adotante,
                        0: self.finalizar}

        while True:  # no exemplo ta como 'continua'
            funcao_escolhida = lista_opcoes[self.__telaAdotante.tela_opcoes()]
            funcao_escolhida()
