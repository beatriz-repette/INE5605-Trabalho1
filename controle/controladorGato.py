from entidade.gato import Gato
from limite.telaGato import TelaGato
from entidade.vacinacao import Vacinacao, Vacina
from exception.erroVacinaException import ErroVacinaException

class ControladorGato():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__telaGato = TelaGato()
        self.__gatos = []

    @property
    def gatos(self):
        return self.__gatos

    def gato_por_chip(self, id):
        for gato in self.__gatos:
            if gato.num_chip == id:
                return gato
        return 'Gato nao se encontra no sistema.'

    def listar_gatos(self):
        if self.__gatos == []:
            self.__telaGato.mensagem_sem_gatos()
        else:
            for a in self.__gatos:
                nomes_vacinas = []
                for vac in a.vacinas:
                    nomes_vacinas.append(vac.vacina._name_)
                self.__telaGato.mostrar_gato({
                    'animal': a.nome,
                    'chip': a.num_chip,
                    'raca': a.raca,
                    'adotado': self.__controladorPrincipal.controladorAdocao.animal_foi_adotado(a.num_chip),
                    'vacinas': nomes_vacinas
                    })

    def incluir_gato(self, dados):
        cat = Gato(dados['chip'], dados['nome'], dados['raca'], dados['vacinas'])
        self.__gatos.append(cat)
        return cat
    
    def adicionar_vacina(self):
        try:
            dados = self.__telaGato.pegar_vacina()
            gato = self.gato_por_chip(dados[0]['animal'])
            if gato != 'Gato nao se encontra no sistema.':
                for v in dados:
                    gato.add_vacina(self.__controladorPrincipal.controladorVacinacao.incluir_vacinacao(v['data'], v['nome'], v['animal']))
            else:
                raise ErroVacinaException
        except:
            self.__telaGato.mensagem_erro_vacina()
    
    def alterar_gato(self):
        chip = self.__telaGato.seleciona_gato()
        gato = self.gato_por_chip(chip)
        if gato != 'Gato nao se encontra no sistema.':
            dados = self.__telaGato.pegar_dados_gato()
            # Se for *, não substitui o valor antigo
            if dados['chip'] != '*':
                if (self.__controladorPrincipal.animal_por_chip(dados['chip']) == 'Animal não se encontra no sistema.'
                    or dados['chip'] == gato.num_chip):
                    doacao = self.__controladorPrincipal.controladorDoacao
                    for doa in doacao.doacoes:
                        if doa.animal == gato.num_chip:
                            doa.animal = dados['chip']
                    gato.num_chip = dados['chip']

                else:
                    self.__telaGato.mostrar_mensagem('Ja existe um animal com esse chip.')
            else:
                # Coloca o chip como o atual para usar na vacinacao
                dados['chip'] = gato.num_chip

            if dados['nome'] != '*':
                gato.nome = dados['nome']

            if dados['raca'] != '*':
                gato.raca = dados['raca']

            if dados['vacinas'] != '*':
                for vac in self.__controladorPrincipal.controladorVacinacao.vacinacoes:
                    if vac.animal_chip == chip:
                        self.__controladorPrincipal.controladorVacinacao.excluir_vacinacao(vac)
                for vac in gato.vacinas:
                    gato.excluir_vacina(vac)

                for v in dados['vacinas']:
                    vacina = self.__controladorPrincipal.controladorVacinacao.incluir_vacinacao(v['data'], v['nome'], dados['chip'])
                    gato.add_vacina(vacina)

            self.__telaGato.mensagem_operacao_concluida()

        else:
            self.__telaGato.mostrar_mensagem(gato)

    def excluir_gato(self):
        chip = self.__telaGato.seleciona_gato()
        gato = self.gato_por_chip(chip)
        if gato != 'Gato nao se encontra no sistema.':
            self.__gatos.remove(gato)
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