from entidade.gato import Gato
from limite.telaGato import TelaGato
from daos.daoGato import GatoDAO
from entidade.vacinacao import Vacinacao, Vacina
from exception.erroVacinaException import ErroVacinaException

class ControladorGato():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__telaGato = TelaGato()
        self.__gato_DAO = GatoDAO()

    @property
    def gatos(self):
        return list(self.__gato_DAO.get_all())

    def gato_por_chip(self, id):
        for gato in self.gatos:
            if gato.num_chip == id:
                return gato
        return 'Gato nao se encontra no sistema.'

    def listar_gatos(self):
        if self.gatos == []:
            self.__telaGato.mensagem_sem_gatos()
        else:
            dados = []
            for a in self.gatos:
                nomes_vacinas = ''
                n = 0
                for vac in a.vacinas:
                    if n < len(a.vacinas)-1:
                        nomes_vacinas += f'{vac.vacina._name_}, '
                    else:
                        nomes_vacinas += vac.vacina._name_
                    n += 1
                dados.append([
                    a.nome,
                    str(a.num_chip),
                    a.raca,
                    nomes_vacinas,
                    'Sim' if self.__controladorPrincipal.controladorAdocao.animal_foi_adotado(a.num_chip) else 'Nao'
                    ])

            self.__telaGato.mostrar_gato(dados)

    def incluir_gato(self, dados):
        # ADICIONAR ESSE FOR EM CACHORRO
        for gato in self.gatos:
            if gato.num_chip == dados['chip']:
                return None
        cat = Gato(dados['chip'], dados['nome'], dados['raca'], dados['vacinas'])
        self.__gato_DAO.add(cat)
        return cat
    
    def adicionar_vacina(self):
        if self.gatos == []:
            self.__telaGato.mensagem_sem_gatos()
        else:
            try:
                chip = self.__telaGato.seleciona_gato()
                if chip == '*':
                    self.__telaGato.mensagem_operacao_cancelada()
                else:
                    gato = self.gato_por_chip(chip)
                    if gato != 'Gato nao se encontra no sistema.':
                        dados = self.__telaGato.pegar_vacina(chip)
                        if dados == 0:
                            self.__telaGato.mensagem_operacao_cancelada()
                        else:
                            gato.add_vacina(self.__controladorPrincipal.controladorVacinacao.incluir_vacinacao(dados['data'], dados['nome'], dados['animal']))
                            self.__gato_DAO.update(gato, gato.num_chip)
                    else:
                        raise ErroVacinaException
            except:
                self.__telaGato.mensagem_erro_vacina()
    
    def alterar_gato(self):
        if self.gatos == []:
            self.__telaGato.mensagem_sem_gatos()
        else:
            chip = self.__telaGato.seleciona_gato()
            gato = self.gato_por_chip(chip)
            if gato != 'Gato nao se encontra no sistema.':
                dados = self.__telaGato.pegar_dados_gato()
                if dados != 0:
                
                    # Se dados['dado'] for *, não substitui o valor antigo
                    if dados['chip'] != '*':
                        # Se o chip não existir ou for o próprio
                        if (self.__controladorPrincipal.animal_por_chip(dados['chip']) == 'Animal não se encontra no sistema.'
                            or dados['chip'] == gato.num_chip):
                            doacao = self.__controladorPrincipal.controladorDoacao
                            for doa in doacao.doacoes:
                                if doa.animal == gato.num_chip:
                                    # ISSO VAI MUDAR QUANDO MUDAR DOACAO
                                    doa.animal = dados['chip']
                            gato.num_chip = dados['chip']

                        else:
                            self.__telaGato.mostrar_mensagem('Ja existe um animal com esse chip.')

                    if dados['nome'] != '*':
                        gato.nome = dados['nome']

                    if dados['raca'] != '*':
                        gato.raca = dados['raca']

                    if dados['vacinas'] != '*':
                        for vac in self.__controladorPrincipal.controladorVacinacao.vacinacoes:
                            if vac.animal_chip == chip:
                                self.__controladorPrincipal.controladorVacinacao.excluir_vacinacao(vac)
                        for vac in gato.vacinas:
                            if vac != '':
                                gato.excluir_vacina(vac)

                        for v in dados['vacinas']:
                            if v['data'] != '':
                                vacina = self.__controladorPrincipal.controladorVacinacao.incluir_vacinacao(v['data'], v['nome'], gato.num_chip)
                                gato.add_vacina(vacina)

                    self.__gato_DAO.update(gato, chip)
                    self.__telaGato.mensagem_operacao_concluida()
                else:
                    self.__telaGato.mensagem_operacao_cancelada()
            else:
                self.__telaGato.mostrar_mensagem(gato)

    def excluir_gato(self):
        if self.gatos == []:
            self.__telaGato.mensagem_sem_gatos()
        else:
            chip = self.__telaGato.seleciona_gato()
            gato = self.gato_por_chip(chip)
            if gato != 'Gato nao se encontra no sistema.':
                self.__gato_DAO.remove(gato.num_chip)
            else:
                self.__telaGato.mostrar_mensagem(gato)

    def finalizar(self):
        self.__controladorPrincipal.controladorAnimal.abrir_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.listar_gatos,
            2: self.adicionar_vacina,
            3: self.alterar_gato,
            4: self.excluir_gato
            }
        while True:
            opcao = self.__telaGato.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()