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
                raise RetornarException

            adotante_de_maior = False
            adotante = None
            for adot in self.__controladorPrincipal.controladorAdotante.adotantes:
                if adot.cpf == dados['cpf']:
                    adotante = adot
                    if adot.data_nascimento < datetime(date.today().year-18, date.today().month, date.today().day):
                            adotante_de_maior = True
            if adotante is None:
                self.__telaAdocao.mensagem_sem_adotante()
                raise ErroRegistroException
            if not adotante_de_maior:
                self.__telaAdocao.mensagem_menor_idade()
                raise ErroRegistroException

            adotante_ja_doou = False
            for doacao in self.__controladorPrincipal.controladorDoacao.doacoes:
                if doacao.doador == dados['cpf']:
                    adotante_ja_doou = True
            if adotante_ja_doou:
                self.__telaAdocao.mensagem_ja_doou()
                raise ErroRegistroException

            animal = self.__controladorPrincipal.animal_por_chip(dados['animal'])
            if animal == 'Animal não se encontra no sistema.':
                self.__telaAdocao.mensagem_no_animal()
                raise ErroRegistroException

            vacinas_animal = []
            for vac in animal.vacinas:
                if vac.vacina._name_ in ['RAIVA', 'HEPATITE', 'LEPTOSPIROSE']:
                    vacinas_animal.append(vac.vacina._name_)
            if sorted(vacinas_animal) != sorted(['RAIVA', 'HEPATITE', 'LEPTOSPIROSE']):
                self.__telaAdocao.mensagem_vacs_invalidas()
                raise ErroRegistroException
            
            if adotante.tipo_habitacao == Habitacao(2) and isinstance(animal, Cachorro) and animal.tamanho in ['g', 'G']:
                self.__telaAdocao.mensagem_residencia_incompativel()
                raise ErroRegistroException

            self.__adocoes.append(Adocao(dados['data'], dados['animal'], dados['cpf'], dados['assinou_termo']))
            self.__telaAdocao.mensagem_operacao_concluida()
        except ErroRegistroException or RetornarException:
            self.__telaAdocao.mensagem_operacao_cancelada()

    def listar_adocoes(self):
        if self.__adocoes == []:
            self.__telaAdocao.mensagem_sem_adocoes()
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


