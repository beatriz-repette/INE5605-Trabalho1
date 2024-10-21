from abc import ABC, abstractmethod
#Decidir se vamos usar classes abstratas ou nao


class TelaAbstrata(ABC):

    @abstractmethod
    def tela_opcoes(self):
        #Printar as opcoes da tela de cada classe
        opcao = input("Escolha a opcao: ")
        while opcao not in []: #Adicionar lista de opcoes validas para cada tela
            print("Input invalido, por favor digite uma das opcoes validas")
            opcao = input("Escolha a opcao: ")

        return int(opcao)
    
    #Inserir, tambem, funcoes de selecionar_itens e pegar_dados_itens para "itens" de cada classe
