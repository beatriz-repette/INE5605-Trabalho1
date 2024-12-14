from entidade.cachorro import Cachorro
from limite.telaCachorro import TelaCachorro
from exception.erroVacinaException import ErroVacinaException
from daos.daoCachorro import CachorroDAO


class ControladorCachorro():
    from controle.controladorPrincipal import ControladorPrincipal
    def __init__(self, cont_principal) -> None:
        self.__controlador_principal = cont_principal
        self.__tela_cachorro = TelaCachorro()
        self.__cachorro_DAO = CachorroDAO()

    @property
    def cachorros(self):
        return list(self.__cachorro_DAO.get_all())

    def cachorro_por_chip(self, id):
        for cachorro in self.cachorros:
            if cachorro.num_chip == id:
                return cachorro
        return 'Cachorro nao se encontra no sistema.'

    def incluir_cachorro(self, dados):
        for cachorro in self.cachorros:
            if cachorro.num_chip == dados['chip']:
                return None
        dog = Cachorro(dados['chip'], dados['nome'], dados['raca'], dados['tamanho'], dados['vacinas'])
        self.__cachorro_DAO.add(dog)
        return dog

    def adicionar_vacina(self):
        if self.cachorros == []:
            self.__tela_cachorro.mensagem_sem_cachorros()
        else:
            try:
                chip = self.__tela_cachorro.seleciona_cachorro()
                if chip == '*':
                    self.__telaGato.mensagem_operacao_cancelada()
                else:
                    cachorro = self.cachorro_por_chip(chip)
                    if cachorro != 'Cachorro nao se encontra no sistema.':
                        dados = self.__tela_cachorro.pegar_vacina(chip)
                        if dados == 0:
                            self.__tela_cachorro.mensagem_operacao_cancelada()
                        else:
                            cachorro.add_vacina(
                                self.__controlador_principal.controladorVacinacao.incluir_vacinacao(dados['data'],
                                                                                                    dados['nome'],
                                                                                                    dados['animal']))
                            self.__cachorro_DAO.update(cachorro, chip)
                    else:
                        raise ErroVacinaException
            except:
                self.__tela_cachorro.mensagem_erro_vacina()

    def alterar_cachorro(self):
        if self.cachorros == []:
            self.__tela_cachorro.mensagem_sem_cachorros()
        else:
            chip = self.__tela_cachorro.seleciona_cachorro()
            cachorro = self.cachorro_por_chip(chip)
            if cachorro != 'Cachorro nao se encontra no sistema.':
                dados = self.__tela_cachorro.pegar_dados_cachorro()
                if dados != 0:

                    # Se for *, não substitui o valor antigo
                    if dados['chip'] != '*':
                        if (self.__controlador_principal.animal_por_chip(
                                dados['chip']) == 'Animal não se encontra no sistema.'
                                or dados['chip'] == cachorro.num_chip):
                            cachorro.num_chip = dados['chip']
                        else:
                            self.__tela_cachorro.mostrar_mensagem('Ja existe um animal com esse chip.')

                    if dados['nome'] != '*':
                        cachorro.nome = dados['nome']

                    if dados['raca'] != '*':
                        cachorro.raca = dados['raca']

                    if dados['tamanho'] != '*':
                        cachorro.tamanho = dados['tamanho']

                    if dados['vacinas'] != '*':
                        for vac in self.__controlador_principal.controladorVacinacao.vacinacoes:
                            if vac.animal_chip == chip:
                                self.__controlador_principal.controladorVacinacao.excluir_vacinacao(vac)
                        for vac in cachorro.vacinas:
                            cachorro.excluir_vacina(vac)

                        for v in dados['vacinas']:
                            vacina = self.__controlador_principal.controladorVacinacao.incluir_vacinacao(v['data'],
                                                                                                         v['nome'],
                                                                                                         cachorro.num_chip)
                            cachorro.add_vacina(vacina)

                    self.__cachorro_DAO.update(cachorro, chip)
                    self.__tela_cachorro.mensagem_operacao_concluida()
                else:
                    self.__tela_cachorro.mensagem_operacao_cancelada()
            else:
                self.__tela_cachorro.mostrar_mensagem(cachorro)

    def listar_cachorros(self):
        if self.cachorros == []:
            self.__tela_cachorro.mensagem_sem_cachorros()
        else:
            dados = []
            for a in self.cachorros:
                nomes_vacinas = ''
                n = 0
                for vac in a.vacinas:
                    if n < len(a.vacinas) - 1:
                        nomes_vacinas += f'{vac.vacina._name_}, '
                    else:
                        nomes_vacinas += vac.vacina._name_
                    n += 1
                dados.append([
                    a.nome,
                    str(a.num_chip),
                    a.tamanho,
                    a.raca,
                    nomes_vacinas,
                    'Sim' if self.__controlador_principal.controladorAdocao.animal_foi_adotado(a.num_chip) else 'Nao'
                ])

            self.__tela_cachorro.mostrar_cachorro(dados)

    def excluir_cachorro(self):
        if self.cachorros == []:
            self.__tela_cachorro.mensagem_sem_cachorros()
        else:
            chip = self.__tela_cachorro.seleciona_cachorro()
            cachorro = self.cachorro_por_chip(chip)
            if cachorro != 'Cachorro nao se encontra no sistema.':
                self.__cachorro_DAO.remove(chip)
            else:
                self.__tela_cachorro.mostrar_mensagem(cachorro)

    def finalizar(self):
        self.__controlador_principal.controladorAnimal.abrir_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.listar_cachorros,
            2: self.adicionar_vacina,
            3: self.alterar_cachorro,
            4: self.excluir_cachorro
        }
        while True:
            opcao = self.__tela_cachorro.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
