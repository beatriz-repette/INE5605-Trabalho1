from entidade.cachorro import Cachorro
from limite.telaCachorro import TelaCachorro

class ControladorCachorro():
    from controle.controladorPrincipal import ControladorPrincipal
    def __init__(self, cont_principal) -> None:
        self.__controladorPrincipal = cont_principal
        self.__telaCachorro = TelaCachorro()
        self.__cachorros = []

    def incluir_cachorro(self, dados):
        dog = Cachorro(dados['chip'], dados['nome'], dados['raca'], dados['tamanho'], dados['vacinas'])
        self.__cachorros.append(dog)
        return dog
    
    def cachorro_por_chip(self, id):
        for cachorro in self.__cachorros:
            if cachorro.chip_id == id:
                return cachorro
        return 'Cachorro nao se encontra no sistema.'

    @property
    def cachorros(self):
        return self.__cachorros
    
    def listar_cachorros(self):
        if self.__cachorros == []:
            self.__telaCachorro.mensagem_sem_cachorros()
        else:
            for a in self.__cachorros:
                self.__telaCachorro.mostrar_cachorro({
                    'animal': a.nome,
                    'chip': a.num_chip,
                    'raca': a.raca,
                    'tamanho': a.tamanho,
                    'adotado': self.__controladorPrincipal.controladorAdocao.animal_foi_adotado(a.num_chip)
                    })

    def finalizar(self):
        self.__controladorPrincipal.controladorAnimal.abrir_tela()

    def abrir_tela(self):
        switch = {
            0: self.finalizar,
            1: self.listar_cachorros,
            }
        while True:
            opcao = self.__telaCachorro.tela_opcoes()
            funcao_escolhida = switch[opcao]
            funcao_escolhida()
