from entidade.vacinacao import Vacinacao, Vacina
from limite.telaVacinacao import TelaVacinacao

class ControladorVacinacao():
    def __init__(self, contPrincipal) -> None:
        self.__controladorPrincipal = contPrincipal
        self.__telaVacinacao = TelaVacinacao()
        self.__vacinacoes = []

    @property
    def vacinacoes(self):
        return self.__vacinacoes
    
    def vacinacao_por_chip_vacina_data(self, chip, vacina, data):
        for vac in self.__vacinacoes:
            if vac.animal_chip == chip and vac.vacina._name_ == vacina and vac.data == data:
                return vac
        return None
    
    def listar_vacinacoes(self):
        for vac in self.__vacinacoes:
            animal = self.__controladorPrincipal.animal_por_chip(vac.animal_chip)
            if animal != 'Animal não se encontra no sistema.':
                self.__telaVacinacao.mostrar_vacinacao({
                    'data': vac.data,
                    'nome': vac.vacina._name_,
                    'animal': animal.nome
                })
            else:
                self.__telaVacinacao.mostrar_vacinacao({
                    'data': vac.data,
                    'nome': vac.vacina._name_,
                    'animal': '[Animal nao encontrado]'
                })
            
    
    def incluir_vacinacao(self, data, vacina, chip):
        vacinacao = Vacinacao(data, Vacina(vacina), chip)
        self.__vacinacoes.append(vacinacao)
        return vacinacao

    # Vai parecer redundante com incluir vacinacao
    # Mas o registrar é pra tela
    # E o incluir pra controladores
    def registrar_vacinacao(self):
        try:
            dados = self.__telaVacinacao.pegar_vacina()
            animal = self.__controladorPrincipal.animal_por_chip(dados[0]['animal'])
            if animal != 'Animal nao se encontra no sistema.':
                for v in dados:
                    animal.add_vacina(self.incluir_vacinacao(v['data'],v['nome'], v['animal']))
            else:
                raise ValueError
        except:
            self.__telaVacinacao.mostrar_mensagem("Erro ao registrar vacinacao.")
    
    def excluir_vacinacao(self, vac = None):

        if vac is None:
            vac = self.__telaVacinacao.selecionar_vacinacao()
            vac = self.vacinacao_por_chip_vacina_data(vac['chip'], vac['vacina'], vac['data'])
        if vac is not None:
            animal = self.__controladorPrincipal.animal_por_chip(vac.animal_chip)
            if animal != 'Animal não se encontra no sistema.':
                self.__vacinacoes.remove(vac)
                animal.excluir_vacina(vac)

    def finalizar(self):
        self.__controladorPrincipal.abre_tela()

    def abre_tela(self):
        switch  = {
            0: self.finalizar,
            1: self.listar_vacinacoes,
            2: self.registrar_vacinacao,
            3: self.excluir_vacinacao
        }

        while True:
            opcao = self.__telaVacinacao.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
