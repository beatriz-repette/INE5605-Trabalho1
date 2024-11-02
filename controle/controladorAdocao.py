from entidade.adocao import Adocao
from entidade.habitacao import Habitacao
from entidade.cachorro import Cachorro
from entidade.gato import Gato
from entidade.vacina import Vacina
from entidade.vacinacao import Vacinacao
from limite.telaAdocao import TelaAdocao
from controle.controladorPrincipal import ControladorPrincipal
from exception.CPFexception import CPFExecption
from datetime import datetime, date


class ControladorAdocao():
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__tela = TelaAdocao()
        self.__adocoes = []

    def incluir_adocao(self):
        try:
            dados = self.__tela.pega_dados_adocao()
            if dados == 0:
                raise Exception

            adotante_de_maior = False
            adotante = None
            for adot in self.__controladorPrincipal.controladorAdotante.adotantes:
                if adot.cpf == dados['cpf']:
                    adotante = adot
                    if adot.data_nascimento < datetime(date.today().year-18, date.today().month, date.today().day):
                            adotante_de_maior = True
            if adotante is None:
                print('Adotante nao se encontra no sistema.')
                raise Exception
            if not adotante_de_maior:
                print('Adotante menor de idade.')
                raise Exception

            adotante_ja_doou = False
            for doacao in self.__controladorPrincipal.controladorDoacao.doacoes:
                if doacao.doador == dados['cpf']:
                    adotante_ja_doou = True
            if adotante_ja_doou:
                print('Adotante ja doou um animal.')
                raise Exception

            animal = self.__controladorPrincipal.animal_por_chip(dados['animal'])
            if animal == 'Animal não se encontra no sistema.':
                print('Animal nao se encontra no sistema.')
                raise Exception

            vacinas_animal = []
            for vac in animal.vacinas:
                if vac.vacina._name_ in ['RAIVA', 'HEPATITE', 'LEPTOSPIROSE']:
                    vacinas_animal.append(vac.vacina._name_)
            if sorted(vacinas_animal) != sorted(['RAIVA', 'HEPATITE', 'LEPTOSPIROSE']):
                print('Vacinas invalidas.')
                raise Exception
            
            if adotante.tipo_habitacao == Habitacao(2) and isinstance(animal, Cachorro) and animal.tamanho in ['g', 'G']:
                print('Tamanho do animal incompativel com a sua residencia.')
                raise Exception

            self.__adocoes.append(Adocao(dados['data'], dados['animal'], dados['cpf'], dados['assinou_termo']))
            print('Adocao realizada! :)')
        except:
            print('Erro ao realizar a adocao.')

    def listar_adocoes(self):
        if self.__adocoes == []:
            print('Nao existem adocoes no sistema.')
        else:
            for a in self.__adocoes:
                animal = self.__controladorPrincipal.animal_por_chip(a.animal)
                self.__tela.mostrar_adocao({
                    'data': a.data_adocao,
                    'animal': animal.nome,
                    'chip': animal.num_chip,
                    'cpf': a.adotante,
                    'assinou_termo': a.termo_responsabilidade
                    })
                
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
            2: self.listar_adocoes,
            }
        while True:
            opcao = self.__tela.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()


