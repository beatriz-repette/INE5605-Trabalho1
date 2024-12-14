from entidade.doacao import Doacao
from entidade.vacinacao import Vacinacao
from entidade.vacina import Vacina
from entidade.animal import Animal
from limite.telaDoacao import TelaDoacao
from exception.erroRegistroException import ErroRegistroException
from exception.retornarException import RetornarException
from exception.chipException import ChipException
from daos.daoDoacao import DoacaoDAO

class ControladorDoacao():
    def __init__(self, cont_principal) -> None:
        self.__controlador_principal = cont_principal
        self.__tela_doacao = TelaDoacao()
        self.__doacao_DAO = DoacaoDAO()

    @property
    def doacoes(self):
        return list(self.__doacao_DAO.get_all())

    def incluir_doacao(self):
        try:
            dados = self.__tela_doacao.pega_dados_doacao()
            if dados == 0:
                self.__tela_doacao.mensagem_operacao_cancelada()
                raise RetornarException

            doador_no_sistema = False
            for doador in self.__controlador_principal.controladorDoador.doadores:
                if doador.cpf == dados['cpf']:
                    doador_no_sistema = True

            if not doador_no_sistema:
                raise ErroRegistroException

            animal = None

            vacinacoes = []

            for v in dados['animal']['vacinas']:
                vacinacoes.append(self.__controlador_principal.controladorVacinacao.incluir_vacinacao(v['data'], v['nome'], v['animal']))
            dados['animal']['vacinas'] = vacinacoes

            if dados['animal']['tipo'] == 'cachorro':
                animal = self.__controlador_principal.controladorCachorro.incluir_cachorro(dados['animal'])
            elif dados['animal']['tipo'] == 'gato':
                animal = self.__controlador_principal.controladorGato.incluir_gato(dados['animal'])

            if animal is None:
                raise ChipException

            # MUDAR ANIMAL PARA UM OBJ ANIMAL E DOADOR
            self.__doacao_DAO.add(Doacao(dados['data'], dados['animal']['chip'], dados['cpf'], dados['motivo']), len(self.doacoes)+1)
            self.__tela_doacao.mensagem_operacao_concluida()

        except ChipException:
            self.__tela_doacao.mensagem('Erro ao registrar doacao: Ja existe um animal com esse chip no sistema.')
        except ErroRegistroException:
            self.__tela_doacao.mensagem("Erro ao registrar doacao: Doador nao encontrado no sistema")
        except:
            self.__tela_doacao.mensagem('Erro ao registrar doacao.')

    def listar_doacoes(self):
        if self.doacoes == []:
            self.__tela_doacao.mensagem("Nao existem adocoes cadastradas no sistema")
        else:
            dados_tabela = []
            n = 1
            for a in self.doacoes:
                try:
                    animal = self.__controlador_principal.controladorAnimal.animal_por_chip(a.animal)
                    linha = {
                        'n': n,
                        'animal': animal.nome if animal != 'Animal não se encontra no sistema.' else '[Animal nao encontrado]',
                        'data': a.data_doacao.strftime("%d/%m/%Y"),
                        'chip': a.animal,
                        'cpf': a.doador,
                        'motivo': a.motivo,
                    }
                    dados_tabela.append(linha)
                    n += 1
                except:
                    pass
            self.__tela_doacao.mostrar_doacao(dados_tabela)

    def excluir_doacao(self):
        if self.doacoes != []:
            doacao = self.__tela_doacao.seleciona_doacao(len(self.doacoes))
            try:
                if doacao == 0:
                        self.__tela_doacao.mensagem_operacao_cancelada()
                        raise RetornarException
                self.__doacao_DAO.remove(doacao)
                self.__tela_doacao.mensagem_operacao_concluida()
            except:
                pass
        else:
            self.__tela_doacao.mensagem('Nao existem doacoes registradas no sistema.')

    def alterar_doacao(self):
        if self.doacoes != []:
            try:
                posicao = self.__tela_doacao.seleciona_doacao(len(self.doacoes))
                if posicao == 0:
                    self.__tela_doacao.mensagem_operacao_cancelada()
                    raise RetornarException
                doacao = self.doacoes[posicao-1]
                novos_dados_doacao = self.__tela_doacao.pega_dados_alterados_doacao()
                if novos_dados_doacao == 0:
                    self.__tela_doacao.mensagem_operacao_cancelada()
                    raise RetornarException

                if novos_dados_doacao["cpf"] != '*':
                    doador_no_sistema = self.__controlador_principal.controladorDoador.doador_por_cpf(novos_dados_doacao['cpf'])
                    if doador_no_sistema is None and novos_dados_doacao["cpf"] != '*':
                        self.__tela_doacao.mensagem("Doador nao encontrado no sistema")
                        self.__tela_doacao.mensagem_operacao_cancelada()
                        raise ErroRegistroException
                    doacao.doador = novos_dados_doacao["cpf"]

                if novos_dados_doacao["data"] != '*':
                    doacao.data_doacao = novos_dados_doacao["data"]

                if novos_dados_doacao["motivo"] != '*':
                    doacao.motivo = novos_dados_doacao["motivo"]

                self.__doacao_DAO.update(doacao, posicao)
                self.__tela_doacao.mensagem_operacao_concluida()

            except:
                pass
        else:
            self.__tela_doacao.mensagem('Nao existem doacoes registradas no sistema.')

    def relatorio_doacao(self):
        if self.doacoes == []:
            self.__tela_doacao.mensagem("Nao existem doacoes cadastradas no sistema")
        else:
            periodo = self.__tela_doacao.seleciona_periodo()
            if periodo != 0:
                n = 1
                dados_tabela = []
                for d in self.doacoes:
                    animal = self.__controlador_principal.controladorAnimal.animal_por_chip(d.animal)
                    if (d.data_doacao >= periodo['inicio']
                        and d.data_doacao <= periodo['fim']):

                        dados_tabela.append({
                            'n': n,
                            'data': d.data_doacao,
                            'animal': animal.nome if animal != 'Animal não se encontra no sistema.' else '[Animal nao encontrado]',
                            'chip': d.animal,
                            'cpf': d.doador,
                            'motivo': d.motivo
                            })
                    n += 1
                if dados_tabela != []:  # Verifica se há adoções no período selecionado
                    self.__tela_doacao.mostrar_doacao(dados_tabela)
                else:
                    self.__tela_doacao.mensagem("Nao existem doacoes no periodo selecionado")
            else:
                self.__tela_doacao.mensagem_operacao_cancelada()

    def finalizar(self):
        self.__controlador_principal.abre_tela()

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
            opcao = self.__tela_doacao.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
