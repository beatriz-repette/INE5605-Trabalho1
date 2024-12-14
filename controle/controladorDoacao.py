from entidade.doacao import Doacao
from entidade.vacinacao import Vacinacao
from entidade.vacina import Vacina
from entidade.animal import Animal
from limite.telaDoacao import TelaDoacao
from exception.erroRegistroException import ErroRegistroException
from exception.retornarException import RetornarException
from exception.chipException import ChipException


class ControladorDoacao():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__telaDoacao = TelaDoacao()
        self.__doacoes = []

    @property
    def doacoes(self):
        return self.__doacoes

    def incluir_doacao(self):
        try:
            dados = self.__telaDoacao.pega_dados_doacao()
            if dados == 0:
                self.__telaDoacao.mensagem_operacao_cancelada()
                raise RetornarException

            doador_no_sistema = False
            for doador in self.__controladorPrincipal.controladorDoador.doadores:
                if doador.cpf == dados['cpf']:
                    doador_no_sistema = True

            if not doador_no_sistema:
                self.__telaDoacao.mensagem("Doador nao encontrado no sistema")
                self.__telaDoacao.mensagem_operacao_cancelada()
                raise ErroRegistroException

            animal = None

            vacinacoes = []

            for v in dados['animal']['vacinas']:
                vacinacoes.append(self.__controladorPrincipal.controladorVacinacao.incluir_vacinacao(v['data'], v['nome'], v['animal']))
            dados['animal']['vacinas'] = vacinacoes

            if dados['animal']['tipo'] == 'cachorro':
                animal = self.__controladorPrincipal.controladorCachorro.incluir_cachorro(dados['animal'])
            elif dados['animal']['tipo'] == 'gato':
                animal = self.__controladorPrincipal.controladorGato.incluir_gato(dados['animal'])

            if animal is None:
                raise ChipException

            # MUDAR ANIMAL PARA UM OBJ ANIMAL E DOADOR
            self.__doacoes.append(Doacao(dados['data'], dados['animal']['chip'], dados['cpf'], dados['motivo']))

            self.__telaDoacao.mensagem_operacao_concluida()

        except ChipException:
            self.__telaDoacao.mensagem('Ja existe um animal com esse chip no sistema.')
        except:
            pass

    def listar_doacoes(self):
        if self.__doacoes == []:
            self.__telaDoacao.mensagem("Nao existem doacoes cadastradas no sistema")
        else:
            n = 0
            for d in self.__doacoes:
                animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(d.animal)
                if animal != 'Animal não se encontra no sistema.':
                    self.__telaDoacao.mostrar_doacao({
                        'data': d.data_doacao,
                        'animal': animal.nome,
                        'chip': d.animal,
                        'cpf': d.doador,
                        'motivo': d.motivo
                        }, n)
                else:
                    self.__telaDoacao.mostrar_doacao({
                        'data': d.data_doacao,
                        'animal': '[Animal nao encontrado]',
                        'chip': d.animal,
                        'cpf': d.doador,
                        'motivo': d.motivo
                        }, n)
                n += 1

    def excluir_doacao(self):
        try:
            doacao = self.__telaDoacao.seleciona_doacao(len(self.__doacoes))
            if doacao == '*':
                    self.__telaDoacao.mensagem_operacao_cancelada()
                    raise RetornarException
            self.__doacoes.remove(self.__doacoes[doacao])
            self.__telaDoacao.mensagem_operacao_concluida()
        except:
            pass

    def alterar_doacao(self):
        try:
            doacao = self.__telaDoacao.seleciona_doacao(len(self.__doacoes))
            if doacao == '*':
                self.__telaDoacao.mensagem_operacao_cancelada()
                raise RetornarException
            doacao = self.__doacoes[doacao]
            novos_dados_doacao = self.__telaDoacao.pega_dados_alterados_doacao()
            if novos_dados_doacao == 0:
                self.__telaDoacao.mensagem_operacao_cancelada()
                raise RetornarException

            if novos_dados_doacao["cpf"] != '*':
                doador_no_sistema = self.__controladorPrincipal.controladorDoador.doador_por_cpf(novos_dados_doacao['cpf'])
                if doador_no_sistema is None and novos_dados_doacao["cpf"] != '*':
                    self.__telaDoacao.mensagem("Doador nao encontrado no sistema")
                    self.__telaDoacao.mensagem_operacao_cancelada()
                    raise ErroRegistroException
                doacao.doador = novos_dados_doacao["cpf"]

            if novos_dados_doacao["chip"] != '*':
                animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(doacao.animal)
                if self.__controladorPrincipal.controladorAnimal.animal_por_chip(novos_dados_doacao['chip']) == 'Animal não se encontra no sistema.':
                    animal.num_chip = novos_dados_doacao["chip"]
                doacao.animal = novos_dados_doacao["chip"]

            if novos_dados_doacao["data"] != '*':
                doacao.data_doacao = novos_dados_doacao["data"]

            if novos_dados_doacao["motivo"] != '*':
                doacao.motivo = novos_dados_doacao["motivo"]

            self.__telaDoacao.mensagem_operacao_concluida()

        except:
            pass

    def relatorio_doacao(self):
        if self.__doacoes == []:
            self.__telaDoacao.mensagem("Nao existem doacoes cadastradas no sistema")
        else:
            periodo = self.__telaDoacao.seleciona_periodo()
            n = 0
            for d in self.__doacoes:
                animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(d.animal)
                if (animal != 'Animal não se encontra no sistema.'
                    and d.data_doacao >= periodo['inicio']
                    and d.data_doacao <= periodo['fim']):

                    self.__telaDoacao.mostrar_doacao({
                        'data': d.data_doacao,
                        'animal': animal.nome,
                        'chip': d.animal,
                        'cpf': d.doador,
                        'motivo': d.motivo
                        }, n)

                elif (animal == 'Animal não se encontra no sistema.'
                    and d.data_doacao >= periodo['inicio']
                    and d.data_doacao <= periodo['fim']):

                    self.__telaDoacao.mostrar_doacao({
                        'data': d.data_doacao,
                        'animal': '[Animal nao encontrado]',
                        'chip': d.animal,
                        'cpf': d.doador,
                        'motivo': d.motivo
                        }, n)
                n += 1

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.incluir_doacao,
            2: self.alterar_doacao,
            3: self.listar_doacoes,
            4: self.excluir_doacao,
            5: self.relatorio_doacao
            }
        while True:
            opcao = self.__telaDoacao.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()


