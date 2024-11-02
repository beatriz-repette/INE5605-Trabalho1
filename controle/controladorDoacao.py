from entidade.doacao import Doacao
from limite.telaDoacao import TelaDoacao
from controle.controladorPrincipal import ControladorPrincipal
from exception.CPFexception import CPFExecption


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
                raise Exception
            doador_no_sistema = False
            for doador in self.__controladorPrincipal.controladorDoador.doadores:
                if doador.cpf == dados['cpf']:
                    doador_no_sistema = True
            if not doador_no_sistema:
                print('Doador nao se encontra no sistema.')
                raise Exception

            animal = None
            if dados['animal']['tipo'] == 'Cachorro':
                animal = self.__controladorPrincipal.controladorCachorro.incluir_cachorro(dados['animal'])
            elif dados['animal']['tipo'] == 'Gato':
                animal = self.__controladorPrincipal.controladorGato.incluir_gato(dados['animal'])
            self.__doacoes.append(Doacao(dados['data'], dados['animal']['chip'], dados['cpf'], dados['motivo']))
        except:
            print('Erro ao realizar a doacao.')

    def listar_doacoes(self):
        if self.__doacoes == []:
            print('Nao existem doacoes no sistema.')
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


