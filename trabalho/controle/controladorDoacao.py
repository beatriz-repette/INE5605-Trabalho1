from entidade import doacao
from entidade.doacao import Doacao
from limite.telaDoacao import TelaDoacao


class ControladorDoacao():
    def __init__(self) -> None:
        from controle.controladorPrincipal import ControladorPrincipal
        self.__controladorPrincipal = ControladorPrincipal
        self.__tela = TelaDoacao()
        self.__doacoes = []

    def incluir_doacao(self):
        dados = self.__tela.pega_dados_doacao()
        animal = None
        if dados['animal']['tipo_animal'] == 'Cachorro':
            animal = self.__controladorPrincipal().controladorCachorro.incluir_cachorro(dados['animal'])
        elif dados['animal']['tipo_animal'] == 'Gato':
            animal = self.__controladorPrincipal().controladorGato.incluir_gato(dados['animal'])
        self.__doacoes.append(Doacao(dados['data'], dados['animal'], dados['cpf'], dados['motivo']))

    def listar_doacoes(self):
        for d in self.__doacoes:
            self.__tela.mostrar_doacao({
                'data': d.data_doacao,
                'animal': d.animal,
                'cpf': d.doador,
                'motivo': d.motivo
                })

    def finalizar(self):
        self.__controladorPrincipal().abre_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.incluir_doacao,
            2: self.listar_doacoes,
            }
        while True:
            opcao = self.__tela.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()


