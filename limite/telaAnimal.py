from limite.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaAnimal(TelaAbstrata):
    def tela_opcoes(self):
        layout = [
        [sg.Radio('Gatos', "RADIO1", key = 1, default = True, size=(10
        ,1))],
        [sg.Radio('Cachorros', "RADIO1", key = 2)],
        [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Animais').Layout(layout)
        button, values = window.Read()
        opcao = 0
        if button != 'Cancel':
            for val in values:
                if values[val]:
                    opcao = val
        window.close()
        return opcao