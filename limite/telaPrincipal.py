from limite.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPrincipal(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()

        if button in (None, 'Cancelar'):
            opcao = 0

        else:
            for val in values:
                if values[val]:
                    opcao = val

        self.__window.Close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGreen')
        layout = [
            [sg.Text("-------- ONG de Animais ---------", font=("Times",25,"bold"))],
            [sg.Text('Escolha sua opção:', font=("Times",15))],
            [sg.Radio('Doador', "RD1", key=1)],
            [sg.Radio('Adotante', "RD1", key=2)],
            [sg.Radio('Doacao', "RD1", key=3)],
            [sg.Radio('Adocao', "RD1", key=4)],
            [sg.Radio('Animais', "RD1", key=5)],
            [sg.Radio('Historico de Vacinacao', "RD1", key=6)],
            [sg.Radio('Finalizar Sistema', "RD1", key=0, default = True)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Menu').Layout(layout)
