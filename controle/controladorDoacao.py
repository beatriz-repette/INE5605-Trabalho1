from entidade.doacao import Doacao
from entidade.vacinacao import Vacinacao
from entidade.vacina import Vacina
from limite.telaDoacao import TelaDoacao
from exception.erroRegistroException import ErroRegistroException
from exception.retornarException import RetornarException


class ControladorDoacao():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__tela = TelaDoacao()
        self.__doacoes = []

    @property
    def doacoes(self):
        return self.__doacoes

    def incluir_doacao(self):
        try:
            dados = self.__tela.pega_dados_doacao()
            if dados == 0:
                self.__tela.mensagem_operacao_cancelada()
                raise RetornarException
            doador_no_sistema = False
            for doador in self.__controladorPrincipal.controladorDoador.doadores:
                if doador.cpf == dados['cpf']:
                    doador_no_sistema = True
            if not doador_no_sistema:
                self.__tela.mensagem_sem_doador()
                self.__tela.mensagem_operacao_cancelada()
                raise ErroRegistroException

            animal = None
            vacinas = []
            for v in dados['animal']['vacinas']:
                vacinas.append(Vacinacao(v['data'], Vacina(v['nome']), v['animal']))
            dados['animal']['vacinas'] = vacinas
            if dados['animal']['tipo'] == 'Cachorro':
                animal = self.__controladorPrincipal.controladorCachorro.incluir_cachorro(dados['animal'])
            elif dados['animal']['tipo'] == 'Gato':
                animal = self.__controladorPrincipal.controladorGato.incluir_gato(dados['animal'])
            self.__doacoes.append(Doacao(dados['data'], dados['animal']['chip'], dados['cpf'], dados['motivo']))
        except ErroRegistroException or ErroRegistroException:
            pass

    def listar_doacoes(self):
        if self.__doacoes == []:
            self.__tela.mensagem_sem_doacoes()
        else:
            for d in self.__doacoes:
                animal = self.__controladorPrincipal.animal_por_chip(d.animal)
                self.__tela.mostrar_doacao({
                    'data': d.data_doacao,
                    'animal': animal.nome,
                    'chip': animal.num_chip,
                    'cpf': d.doador,
                    'motivo': d.motivo
                    })

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

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


