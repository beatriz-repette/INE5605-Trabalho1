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


class ControladorAdocao():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__telaAdocao = TelaAdocao()
        self.__adocoes = []

    def incluir_adocao(self):
        try:
            dados = self.__telaAdocao.pega_dados_adocao()
            if dados == 0:
                self.__telaAdocao.mensagem_operacao_cancelada()
                raise RetornarException

            adotante_de_maior = False
            adotante = None
            for adot in self.__controladorPrincipal.controladorAdotante.adotantes:
                if adot.cpf == dados['cpf']:
                    adotante = adot
                    if adot.data_nascimento < datetime(date.today().year-18, date.today().month, date.today().day):
                            adotante_de_maior = True
            if adotante is None:
                self.__telaAdocao.mensagem("Sem adotantes no sistema")
                raise ErroRegistroException
            if not adotante_de_maior:
                self.__telaAdocao.mensagem("Para realizar uma adocao, o adotante precisa ter mais de 18 anos.")
                raise ErroRegistroException

            adotante_ja_doou = False
            for doacao in self.__controladorPrincipal.controladorDoacao.doacoes:
                if doacao.doador == dados['cpf']:
                    adotante_ja_doou = True
            if adotante_ja_doou:
                self.__telaAdocao.mensagem("Para realizar uma adocao, o adotante nao pode ja ter doado um animal.")
                raise ErroRegistroException

            animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(dados['animal'])
            if animal == 'Animal não se encontra no sistema.':
                self.__telaAdocao.mensagem("Esse animal nao foi encontrado no sistema.")
                raise ErroRegistroException

            vacinas_animal = []
            for vac in animal.vacinas:
                vacinas_animal.append(vac.vacina._name_)
            if sorted(vacinas_animal) != sorted(['RAIVA', 'HEPATITE', 'LEPTOSPIROSE']):
                self.__telaAdocao.mensagem("Esse animal nao possui todas as vacinas necessarias para poder ser adotado.")
                raise ErroRegistroException
            
            if adotante.tipo_habitacao == Habitacao(2) and isinstance(animal, Cachorro) and animal.tamanho in ['g', 'G']:
                self.__telaAdocao.mensagem("Tamanho do animal incompativel com a sua residencia.")
                raise ErroRegistroException

            if self.animal_foi_adotado(animal.num_chip):
                self.__telaAdocao.mensagem("O animal ja foi adotado.")
                raise ErroRegistroException

            self.__adocoes.append(Adocao(dados['data'], dados['animal'], dados['cpf'], dados['assinou_termo']))
            self.__telaAdocao.mensagem_operacao_concluida()
        except:
            pass

    def alterar_adocao(self):
        try:
            adocao = self.__telaAdocao.seleciona_adocao(len(self.__adocoes))
            if adocao == '*':
                self.__telaAdocao.mensagem_operacao_cancelada()
                raise RetornarException
            
            adocao = self.__adocoes[adocao]

            dados = self.__telaAdocao.pega_dados_alterados_adocao()
            if dados == 0:
                self.__telaAdocao.mensagem_operacao_cancelada()
                raise RetornarException

            adotante = None
            animal = None

            if dados['animal'] != '*':
                animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(dados['animal'])
                if animal == 'Animal não se encontra no sistema.':
                    self.__telaAdocao.mensagem("Esse animal nao foi encontrado no sistema.")
                    raise ErroRegistroException
                
                if self.animal_foi_adotado(animal.num_chip) and animal.num_chip != adocao.animal:
                    self.__telaAdocao.mensagem("O animal ja foi adotado.")
                    raise ErroRegistroException
                
                adocao.animal = dados['animal']
            else:
                animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(adocao.animal)
            
            if dados['cpf'] != '*':
                adotante = self.__controladorPrincipal.controladorAdotante.adotante_por_cpf(dados['cpf'])
                if adotante.data_nascimento > datetime(date.today().year-18, date.today().month, date.today().day):
                    self.__telaAdocao.mensagem("Para realizar uma adocao, o adotante precisa ter mais de 18 anos.")
                    raise ErroRegistroException
                if adotante is None:
                    self.__telaAdocao.mensagem("Sem adotantes no sistema")
                    raise ErroRegistroException
                    

                adotante_ja_doou = False
                for doacao in self.__controladorPrincipal.controladorDoacao.doacoes:
                    if doacao.doador == dados['cpf']:
                        adotante_ja_doou = True
                if adotante_ja_doou:
                    self.__telaAdocao.mensagem("Para realizar uma adocao, o adotante nao pode ja ter doado um animal.")
                    raise ErroRegistroException
                
                adocao.adotante = dados['cpf']
            else: 
                adotante = self.__controladorPrincipal.controladorAdotante.adotante_por_cpf(adocao.adotante)

            if dados['data'] != '*':
                adocao.data_adocao = dados['data']

            if dados['assinou_termo'] != '*':
                adocao.assinou_termo = dados['assinou_termo']

            if adotante.tipo_habitacao._name_ == 'APARTAMENTO_PEQUENO' and isinstance(animal, Cachorro) and animal.tamanho in ['g', 'G']:
                self.__telaAdocao.mensagem("Tamanho do animal incompativel com a sua residencia.")
                raise ErroRegistroException

            self.__telaAdocao.mensagem_operacao_concluida()
        except:
            pass

    def listar_adocoes(self):
        if self.__adocoes == []:
            self.__telaAdocao.mensagem("Nao existem adocoes cadastradas no sistema")
        else:
            dados_tabela = []
            for n, a in enumerate(self.__adocoes, start=1):
                animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(a.animal)
                linha = {
                    'N': n,
                    'animal': animal.nome if animal != 'Animal não se encontra no sistema.' else '[Animal nao encontrado]',
                    'data': a.data_adocao.strftime("%d/%m/%Y"),
                    'chip': a.animal,
                    'cpf': a.adotante,
                    'assinou_termo': "SIM" if a.termo_responsabilidade else "NAO",
                }
                dados_tabela.append(linha)
            self.__telaAdocao.mostrar_adocao(dados_tabela)

    def relatorio_adocao(self):
        if self.__adocoes == []:
            self.__telaAdocao.mensagem("Nao existem adocoes cadastradas no sistema")
        else:
            periodo = self.__telaAdocao.seleciona_periodo()
            dados_tabela = []
            for n, a in enumerate(self.__adocoes, start=1):
                if periodo["inicio"] <= a.data_adocao <= periodo["fim"]:
                    animal = self.__controladorPrincipal.controladorAnimal.animal_por_chip(a.animal)
                    linha = {
                        'N': n,
                        'animal': animal.nome if animal != 'Animal não se encontra no sistema.' else '[Animal nao encontrado]',
                        'data': a.data_adocao.strftime("%d/%m/%Y"),
                        'chip': a.animal,
                        'cpf': a.adotante,
                        'assinou_termo': "SIM" if a.termo_responsabilidade else "NAO",
                    }
                    dados_tabela.append(linha)
            if dados_tabela:  # Verifica se há adoções no período selecionado
                self.__telaAdocao.mostrar_adocao(dados_tabela)
            else:
                self.__telaAdocao.mensagem("Nao existem adocoes no periodo selecionado")
    
    def excluir_adocao(self):
        try:
            adocao = self.__telaAdocao.seleciona_adocao(len(self.__adocoes))
            if adocao != '*' and adocao != '0':
                self.__adocoes.remove(self.__adocoes[adocao])
                self.__telaAdocao.mensagem_operacao_concluida()
            else:
                self.__telaAdocao.mensagem_operacao_cancelada()
        except:
            pass
                
    def animal_foi_adotado(self, id):
        for a in self.__adocoes:
            if a.animal == id:
                return True
        return False

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

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
            opcao = self.__telaAdocao.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()


