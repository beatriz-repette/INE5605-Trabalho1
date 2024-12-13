from abc import ABC, abstractmethod
import PySimpleGUI as sg


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

    def mensagem_operacao_cancelada(self):
        sg.popup("Operacao cancelada", title="Cancelado")

    def mensagem_operacao_concluida(self):
        sg.popup("Operacao realizada com sucesso!", title="Sucesso")

    def mensagem(self, m):
        sg.popup(m)

    def collapse(self, lyt, key, visibl):
        """
        Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
        :param layout: The layout for the section
        :param key: Key used to make this section visible / invisible
        :param visible: visible determines if section is rendered visible or invisible on initialization
        :return: A pinned column that can be placed directly into your layout
        :rtype: sg.pin
        """
        return sg.pin(sg.Column(lyt, key=key, visible=visibl, pad=(0,0)))
    
    @abstractmethod
    def tela_opcoes(self): #Anteriormente funcao chamava-se "mostrar_opcoes"
        opcao = self.ler_int('Escolha uma opcao: ', [0])
        return opcao

#Inserir, tambem, funcoes de selecionar_itens e pegar_dados_itens para "itens" de cada classe
