from abc import ABC, abstractmethod


class TelaAbstrata(ABC):
    def ler_int(self, mensagem = '', int_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if int_validos and inteiro not in int_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('Valor incorreto: Digite um valor numerico inteiro valido')

    
    @abstractmethod
    def tela_opcoes(self): #Anteriormente funcao chamava-se "mostrar_opcoes"
        opcao = self.ler_int('Escolha uma opcao: ', [0])
        return opcao

#Inserir, tambem, funcoes de selecionar_itens e pegar_dados_itens para "itens" de cada classe
