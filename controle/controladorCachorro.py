from entidade.cachorro import Cachorro
from limite.telaCachorro import TelaCachorro
from exception.erroVacinaException import ErroVacinaException
from daos.daoCachorro import CachorroDAO

class ControladorCachorro():
    from controle.controladorPrincipal import ControladorPrincipal
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__telaCachorro = TelaCachorro()
        self.__cachorroDAO = CachorroDAO()

    @property
    def cachorros(self):
        return self.__cachorroDAO.get_all()
    
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
        self.__cachorroDAO.add(dog)
        return dog
    
    def adicionar_vacina(self):
        if self.cachorros == []:
            self.__telaCachorro.mensagem_sem_cachorros()
        else:
            try:
                chip = self.__telaCachorro.seleciona_cachorro()
                cachorro = self.cachorro_por_chip(chip)
                if cachorro != 'Cachorro nao se encontra no sistema.':
                    dados = self.__telaCachorro.pegar_vacina(chip)
                    for v in dados:
                        cachorro.add_vacina(self.__controladorPrincipal.controladorVacinacao.incluir_vacinacao(v['data'], v['nome'], v['animal']))
                    self.__cachorroDAO.update(cachorro, chip)
                else:
                    raise ErroVacinaException
            except:
                self.__telaCachorro.mensagem_erro_vacina()

    def alterar_cachorro(self):
        if self.cachorros == []:
            self.__telaCachorro.mensagem_sem_cachorros()
        else:
            chip = self.__telaCachorro.seleciona_cachorro()
            cachorro = self.cachorro_por_chip(chip)
            if cachorro != 'Cachorro nao se encontra no sistema.':
                dados = self.__telaCachorro.pegar_dados_cachorro()
                # Se for *, não substitui o valor antigo
                if dados['chip'] != '*':
                    if (self.__controladorPrincipal.animal_por_chip(dados['chip']) == 'Animal não se encontra no sistema.'
                        or dados['chip'] == cachorro.num_chip):
                        cachorro.num_chip = dados['chip']
                    else:
                        self.__telaCachorro.mostrar_mensagem('Ja existe um animal com esse chip.')

                if dados['nome'] != '*':
                    cachorro.nome = dados['nome']

                if dados['raca'] != '*':
                    cachorro.raca = dados['raca']

                if dados['tamanho'] != '*':
                    cachorro.tamanho = dados['tamanho']

                if dados['vacinas'] != '*':
                    for vac in self.__controladorPrincipal.controladorVacinacao.vacinacoes:
                        if vac.animal_chip == chip:
                            self.__controladorPrincipal.controladorVacinacao.excluir_vacinacao(vac)
                    for vac in cachorro.vacinas:
                        cachorro.excluir_vacina(vac)

                    for v in dados['vacinas']:
                        vacina = self.__controladorPrincipal.controladorVacinacao.incluir_vacinacao(v['data'], v['nome'], cachorro.num_chip)
                        cachorro.add_vacina(vacina)

                self.__cachorroDAO.update(cachorro, chip)
                self.__telaCachorro.mensagem_operacao_concluida()
            else:
                self.__telaCachorro.mostrar_mensagem(cachorro)
    
    def listar_cachorros(self):
        if self.cachorros == []:
            self.__telaCachorro.mensagem_sem_cachorros()
        else:
            dados = []
            for a in self.cachorros:
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
                    a.tamanho,
                    a.raca,
                    nomes_vacinas,
                    'Sim' if self.__controladorPrincipal.controladorAdocao.animal_foi_adotado(a.num_chip) else 'Nao'
                    ])

            self.__telaCachorro.mostrar_cachorro(dados)
                
    def excluir_cachorro(self):
        if self.cachorros == []:
            self.__telaCachorro.mensagem_sem_cachorros()
        else:
            chip = self.__telaCachorro.seleciona_cachorro()
            cachorro = self.cachorro_por_chip(chip)
            if cachorro != 'Cachorro nao se encontra no sistema.':
                self.__cachorroDAO.remove(chip)
            else:
                self.__telaCachorro.mostrar_mensagem(cachorro)

    def finalizar(self):
        self.__controladorPrincipal.controladorAnimal.abrir_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.listar_cachorros,
            2: self.adicionar_vacina,
            3: self.alterar_cachorro,
            4: self.excluir_cachorro
            }
        while True:
            opcao = self.__telaCachorro.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
