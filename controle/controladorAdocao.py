from entidade.adocao import Adocao
from entidade.habitacao import Habitacao
from entidade.cachorro import Cachorro
from entidade.gato import Gato
from entidade.vacina import Vacina
from entidade.vacinacao import Vacinacao
from limite.telaAdocao import TelaAdocao
from datetime import datetime, date
from exception.erroRegistroException import ErroRegistroException
from exception.retornarException import RetornarException
from daos.daoAdocao import AdocaoDAO


class ControladorAdocao():
    def __init__(self, cont_principal) -> None:
        self.__controlador_principal = cont_principal
        self.__tela_adocao = TelaAdocao()
        self.__adocoes_DAO = AdocaoDAO()

    @property
    def adocoes(self):
        return list(self.__adocoes_DAO.get_all())

    def incluir_adocao(self):
        try:
            dados = self.__tela_adocao.pega_dados_adocao()
            if dados == 0:
                self.__tela_adocao.mensagem_operacao_cancelada()
                raise RetornarException

            adotante_de_maior = False
            adotante = None
            for adot in self.__controlador_principal.controladorAdotante.adotantes:
                if adot.cpf == dados['cpf']:
                    adotante = adot
                    if adot.data_nascimento < datetime(date.today().year-18, date.today().month, date.today().day):
                            adotante_de_maior = True
            if adotante is None:
                self.__tela_adocao.mensagem("Sem adotantes no sistema")
                raise ErroRegistroException
            if not adotante_de_maior:
                self.__tela_adocao.mensagem("Para realizar uma adocao, o adotante precisa ter mais de 18 anos.")
                raise ErroRegistroException

            adotante_ja_doou = False
            for doacao in self.__controlador_principal.controladorDoacao.doacoes:
                if doacao.doador == dados['cpf']:
                    adotante_ja_doou = True
            if adotante_ja_doou:
                self.__tela_adocao.mensagem("Para realizar uma adocao, o adotante nao pode ja ter doado um animal.")
                raise ErroRegistroException

            animal = self.__controlador_principal.controladorAnimal.animal_por_chip(dados['animal'])
            if animal == 'Animal não se encontra no sistema.':
                self.__tela_adocao.mensagem("Esse animal nao foi encontrado no sistema.")
                raise ErroRegistroException

            vacinas_animal = []
            for vac in animal.vacinas:
                vacinas_animal.append(vac.vacina._name_)
            if sorted(vacinas_animal) != sorted(['RAIVA', 'HEPATITE', 'LEPTOSPIROSE']):
                self.__tela_adocao.mensagem("Esse animal nao possui todas as vacinas necessarias para poder ser adotado.")
                raise ErroRegistroException

            if adotante.tipo_habitacao == Habitacao(2) and isinstance(animal, Cachorro) and animal.tamanho in ['g', 'G']:
                self.__tela_adocao.mensagem("Tamanho do animal incompativel com a sua residencia.")
                raise ErroRegistroException

            if self.animal_foi_adotado(animal.num_chip):
                self.__tela_adocao.mensagem("O animal ja foi adotado.")
                raise ErroRegistroException
            
            self.__adocoes_DAO.add(Adocao(dados['data'], dados['animal'], dados['cpf'], dados['assinou_termo']), len(self.adocoes)+1)
            self.__tela_adocao.mensagem_operacao_concluida()
        except ErroRegistroException:
            self.__tela_adocao.mensagem('Erro ao registrar adocao.')

    def alterar_adocao(self):
        try:
            id= self.__tela_adocao.seleciona_adocao(len(self.adocoes)) #para o dao
            if adocao == '*':
                self.__tela_adocao.mensagem_operacao_cancelada()
                raise RetornarException

            adocao = self.adocoes[adocao]

            dados = self.__tela_adocao.pega_dados_alterados_adocao()
            if dados == 0:
                self.__tela_adocao.mensagem_operacao_cancelada()
                raise RetornarException

            adotante = None
            animal = None

            if dados['animal'] != '*':
                animal = self.__controlador_principal.controladorAnimal.animal_por_chip(dados['animal'])
                if animal == 'Animal não se encontra no sistema.':
                    self.__tela_adocao.mensagem("Esse animal nao foi encontrado no sistema.")
                    raise ErroRegistroException

                if self.animal_foi_adotado(animal.num_chip) and animal.num_chip != adocao.animal:
                    self.__tela_adocao.mensagem("O animal ja foi adotado.")
                    raise ErroRegistroException

                adocao.animal = dados['animal']
            else:
                animal = self.__controlador_principal.animal_por_chip(adocao.animal)

            if dados['cpf'] != '*':
                adotante = self.__controlador_principal.controladorAdotante.adotante_por_cpf(dados['cpf'])
                if adotante.data_nascimento > datetime(date.today().year-18, date.today().month, date.today().day):
                    self.__tela_adocao.mensagem("Para realizar uma adocao, o adotante precisa ter mais de 18 anos.")
                    raise ErroRegistroException
                if adotante is None:
                    self.__tela_adocao.mensagem("Sem adotantes no sistema")
                    raise ErroRegistroException


                adotante_ja_doou = False
                for doacao in self.__controlador_principal.controladorDoacao.doacoes:
                    if doacao.doador == dados['cpf']:
                        adotante_ja_doou = True
                if adotante_ja_doou:
                    self.__tela_adocao.mensagem("Para realizar uma adocao, o adotante nao pode ja ter doado um animal.")
                    raise ErroRegistroException

                adocao.adotante = dados['cpf']
            else:
                adotante = self.__controlador_principal.controladorAdotante.adotante_por_cpf(adocao.adotante)

            if dados['data'] != '*':
                adocao.data_adocao = dados['data']

            if dados['assinou_termo'] != '*':
                adocao.assinou_termo = dados['assinou_termo']

            if adotante.tipo_habitacao._name_ == 'APARTAMENTO_PEQUENO' and isinstance(animal, Cachorro) and animal.tamanho in ['g', 'G']:
                self.__tela_adocao.mensagem("Tamanho do animal incompativel com a sua residencia.")
                raise ErroRegistroException

            self.__adocoes_DAO.update(id, adocao)
            self.__tela_adocao.mensagem_operacao_concluida()
        except:
            pass

    def listar_adocoes(self):
        if self.adocoes == []:
            self.__tela_adocao.mensagem("Nao existem adocoes cadastradas no sistema")
        else:
            dados_tabela = []
            for n, a in enumerate(self.adocoes, start=1):
                try:
                    animal = self.__controlador_principal.controladorAnimal.animal_por_chip(a.animal)
                    linha = {
                        'n': n,
                        'animal': animal.nome if animal != 'Animal não se encontra no sistema.' else '[Animal nao encontrado]',
                        'data': a.data_adocao.strftime("%d/%m/%Y"),
                        'chip': a.animal,
                        'cpf': a.adotante,
                        'assinou_termo': "SIM" if a.termo_responsabilidade else "NAO",
                    }
                    dados_tabela.append(linha)
                except:
                    self.__tela_adocao.mensagem(n)
            self.__tela_adocao.mostrar_adocao(dados_tabela)

    def relatorio_adocao(self):
        if self.adocoes == []:
            self.__tela_adocao.mensagem("Nao existem adocoes cadastradas no sistema")
        else:
            periodo = self.__tela_adocao.seleciona_periodo()
            dados_tabela = []
            n = 1
            for a in self.adocoes:
                if periodo["inicio"] <= a.data_adocao <= periodo["fim"]:
                    animal = self.__controlador_principal.animal_por_chip(a.animal)
                    linha = {
                        'n': n,
                        'animal': animal.nome if animal != 'Animal não se encontra no sistema.' else '[Animal nao encontrado]',
                        'data': a.data_adocao.strftime("%d/%m/%Y"),
                        'chip': a.animal,
                        'cpf': a.adotante,
                        'assinou_termo': a.termo_responsabilidade
                    }
                    dados_tabela.append(linha)
                    n += 1
            if dados_tabela != []:  # Verifica se há adoções no período selecionado
                self.__tela_adocao.mostrar_adocao(dados_tabela)
            else:
                self.__tela_adocao.mensagem("Nao existem adocoes no periodo selecionado")

    def excluir_adocao(self):
        try:
            adocao = self.__tela_adocao.seleciona_adocao(len(self.adocoes))
            if adocao > 0:
                self.__adocoes_DAO.remove(adocao)
                self.__tela_adocao.mensagem_operacao_concluida()
            else:
                self.__tela_adocao.mensagem_operacao_cancelada()
        except:
            pass

    def animal_foi_adotado(self, id):
        for a in self.adocoes:
            if a.animal == id:
                return True
        return False

    def finalizar(self):
        self.__controlador_principal.abre_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.incluir_adocao,
            2: self.alterar_adocao,
            3: self.listar_adocoes,
            4: self.excluir_adocao,
            5: self.relatorio_adocao
            }
        while True:
            opcao = self.__tela_adocao.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
