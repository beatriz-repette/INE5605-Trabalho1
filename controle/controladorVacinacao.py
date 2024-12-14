from entidade.vacinacao import Vacinacao, Vacina
from limite.telaVacinacao import TelaVacinacao
from exception.chipException import ChipException
from daos.daoVacinacao import VacinacaoDAO
import datetime


class ControladorVacinacao():
    def __init__(self, contPrincipal) -> None:
        self.__controlador_principal = contPrincipal
        self.__tela_vacinacao = TelaVacinacao()
        self.__vacinacao_DAO = VacinacaoDAO()

    @property
    def vacinacoes(self):
        return list(self.__vacinacao_DAO.get_all())

    def vacinacao_por_chip_vacina_data(self, chip, vacina, data):
        key = 0
        for vac in self.vacinacoes:
            if vac.animal_chip == chip and vac.vacina._name_ == vacina and vac.data == data:
                return {'vac': vac, 'key': key}
            key += 1
        return None

    def listar_vacinacoes(self):
        if self.vacinacoes == []:
            self.__tela_vacinacao.mostrar_mensagem('Nao existem vacinacoes no sistema.')
        else:
            dados = []
            for vac in self.vacinacoes:
                animal = self.__controlador_principal.controladorAnimal.animal_por_chip(vac.animal_chip)
                if animal != 'Animal não se encontra no sistema.':
                    dados.append([
                        vac.data.strftime('%d/%m/%Y'),
                        vac.vacina._name_,
                        animal.nome
                    ])
                else:
                    dados.append([
                        vac.data.strftime('%d/%m/%Y'),
                        vac.vacina._name_,
                        '[Animal nao encontrado]'
                    ])
            self.__tela_vacinacao.mostrar_vacinacao(dados)

    def incluir_vacinacao(self, data, vacina, chip):
        vacinacao = Vacinacao(data, Vacina(vacina), chip)
        key = len(self.vacinacoes)
        self.__vacinacao_DAO.add(vacinacao, key)
        return vacinacao

    # Vai parecer redundante com incluir vacinacao
    # Mas o registrar é pra tela
    # E o incluir pra controladores
    def registrar_vacinacao(self):
        chip = self.__tela_vacinacao.seleciona_animal()
        if chip != '*':
            try:
                animal = self.__controlador_principal.animal_por_chip(chip)
                if animal != 'Animal nao se encontra no sistema.':
                    dados = self.__tela_vacinacao.pegar_vacina(chip)
                    if dados == 0:
                        self.__tela_vacinacao.mensagem_operacao_cancelada()
                    else:
                        animal.add_vacina(self.incluir_vacinacao(dados['data'], dados['nome'], dados['animal']))
                        self.__tela_vacinacao.mensagem_operacao_concluida()
                else:
                    raise ValueError
            except ChipException:
                self.__tela_vacinacao.mostrar_mensagem("Por favor, insira um chip valido.")
            except:
                self.__tela_vacinacao.mostrar_mensagem("Erro ao registrar vacinacao.")
        else:
            self.__tela_vacinacao.mensagem_operacao_cancelada()

    def excluir_vacinacao(self, vac=None):
        try:
            if self.vacinacoes == []:
                self.__tela_vacinacao.mostrar_mensagem('Nao existem vacinacoes no sistema.')
            else:
                if vac is None:
                    vac = self.__tela_vacinacao.selecionar_vacinacao()
                if vac != 0:
                    vac = self.vacinacao_por_chip_vacina_data(vac['chip'], vac['vacina'], vac['data'])
                    if vac is not None:
                        self.__vacinacao_DAO.remove(vac['key'])
                        animal = self.__controlador_principal.animal_por_chip(vac['vac'].animal_chip)
                        if animal != 'Animal não se encontra no sistema.':
                            animal.excluir_vacina(vac['vac'])
                        self.__tela_vacinacao.mensagem_operacao_concluida()
                    else:
                        self.__tela_vacinacao.mensagem('Erro ao excluir vacinacao.')
                else:
                    self.__tela_vacinacao.mensagem_operacao_cancelada()
        except:
            pass

    def finalizar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        switch = {
            0: self.finalizar,
            1: self.listar_vacinacoes,
            2: self.registrar_vacinacao,
            3: self.excluir_vacinacao
        }

        while True:
            opcao = self.__tela_vacinacao.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
