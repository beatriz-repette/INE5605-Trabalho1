from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
from exception.erroCadastroException import ErroCadastroException
from exception.chipException import ChipException
from exception.dateException import DateException
import PySimpleGUI as sg


class TelaVacinacao(TelaAbstrata):
    def tela_opcoes(self):
        layout = [
            [sg.Text("-------- Historico de Vacinacao ---------", font=("Times",25,"bold"))],
            [sg.Text('Escolha sua opção:', font=("Times",15))],
            [sg.Radio('Ver vacinacoes', "RADIO1", key = 1, default = True, size=(10
            ,1))],
            [sg.Radio('Adicionar vacinacao', "RADIO1", key = 2)],
            [sg.Radio('Excluir vacinacao', "RADIO1", key = 3)],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Historico de Vacinacao').Layout(layout)
        button, values = window.Read()
        opcao = 0
        if button != 'Cancel':
            for val in values:
                if values[val]:
                    opcao = val
        window.close()
        return opcao
    
    def seleciona_animal(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("Chip do animal que deseja vacinar:"), sg.InputText(key='chip')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                window.Close()
                return '*'

            elif event == "Confirmar":
                try:
                    chip = int((values['chip']))
                    if chip < 0:
                        raise ValueError
                    window.close()
                    return chip
                except:
                    sg.popup("O chip digitado está incorreto, por favor o digite novamente.")
    
    def pegar_vacina(self, chip):
        sg.ChangeLookAndFeel('DarkGreen')
        visivel1 = False
        visivel2 = False
        visivel3 = False

        vac_raiva = [[sg.Input(key = 'data-raiva'),
                      sg.CalendarButton("Selecionar Data", target="data-raiva", format="%d/%m/%Y")]]
        
        vac_hep = [[sg.Input(key = 'data-hepatite'),
                    sg.CalendarButton("Selecionar Data", target="data-hepatite", format="%d/%m/%Y")]]
        
        vac_lepto = [[sg.Input(key = 'data-lepto'),
                      sg.CalendarButton("Selecionar Data", target="data-lepto", format="%d/%m/%Y")]]

        layout = [
            [sg.Text("-------- Dados Vacina ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados da(s) vacina(s):", font=("Times",15))],
            [sg.Checkbox("Vacina da raiva:", enable_events = True, key = 'raiva'),
             self.collapse(vac_raiva, 'sec-raiva', False)],
            [sg.Checkbox("Vacina da hepatite:", enable_events = True, key = 'hepatite'),
             self.collapse(vac_hep, 'sec-hepatite', False)],
            [sg.Checkbox("Vacina da leptospirose:", enable_events = True, key = 'lepto'),
             self.collapse(vac_lepto, 'sec-lepto', False)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                window.Close()
                return 0

            if event == 'raiva':
                visivel1 = not visivel1
                window['sec-raiva'].update(visible = visivel1)

            if event == 'hepatite':
                visivel2 = not visivel2
                window['sec-hepatite'].update(visible = visivel2)

            if event == 'lepto':
                visivel3 = not visivel3
                window['sec-lepto'].update(visible = visivel3)

            if event == "Confirmar":
                try:
                    vacinas_animal = []
                    data_vacina_rai = values['data-raiva']
                    if data_vacina_rai != '':
                        try:
                            data_vacina_rai = datetime.strptime(data_vacina_rai, '%d/%m/%Y')
                        except:
                            raise DateException

                    data_vacina_hep = values['data-hepatite']
                    if data_vacina_hep != '':
                        try:
                            data_vacina_hep = datetime.strptime(data_vacina_hep, '%d/%m/%Y')
                        except:
                            raise DateException

                    data_vacina_lep = values['data-lepto']
                    if data_vacina_lep != '':
                        try:
                            data_vacina_lep = datetime.strptime(data_vacina_lep, '%d/%m/%Y')
                        except:
                            raise DateException

                    if (data_vacina_rai != '' or data_vacina_hep != '' or data_vacina_lep != ''):
                        vacinas_animal.append({'data': data_vacina_rai, 'nome': 1, 'animal': chip})
                        vacinas_animal.append({'data': data_vacina_hep, 'nome': 2, 'animal': chip})
                        vacinas_animal.append({'data': data_vacina_lep, 'nome': 3, 'animal': chip})
                    else:
                        vacinas_animal = '*'
                    window.close()
                    return vacinas_animal
                
                except ErroCadastroException:
                    sg.popup("Nome invalido, por favor digite novamente.")
                except DateException:
                    sg.popup('Por favor, insira uma data de vacina válida.')
    
    def mostrar_vacinacao(self, dados):
        layout = [
            [sg.Text("Lista de Vacinacoes", font=("Times", 25, "bold"))],
            [sg.Table(values=dados,
                      headings=["Data", "Nome da vacina", "Nome do animal"],
                      auto_size_columns=True,
                      justification='center',
                      num_rows=10,
                      key='-TABELA-')],
            [sg.Button("Fechar")]
        ]

        # Criar janela para exibir a tabela
        window = sg.Window("Vacinacoes", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()

    def selecionar_vacinacao(self):
        '''
        return {'chip': chip, 'vacina': vacina, 'data': data_vacina}
        '''
        layout = [
            [sg.Text("-------- Dados Vacinacao ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados da vacinacao:", font=("Times",15))],
            [sg.Text("Chip do animal:"), sg.InputText(key = 'chip')],
            [sg.Text("Nome da vacina:"),
             sg.Radio("Raiva", 'VACINAS', key = 1, default = True),
             sg.Radio("Hepatite", 'VACINAS', key = 2),
             sg.Radio("Leptospirose", 'VACINAS', key = 3)],
            [sg.Text("Data de aplicacao:"),
             sg.Input(enable_events = True, key = 'data'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                window.Close()
                return 0
            
            if event == 'Confirmar':
                chip = values['chip']
                data = values['data']

                try:
                    if chip == '':
                        chip = '*'
                    else:
                        try:
                            chip = int(chip)
                            if chip < 0:
                                raise ChipException
                        except:
                            raise ChipException
                    
                    vacina = 0
                    opcoes = {1: 'RAIVA', 2: 'HEPATITE', 3: 'LEPTOSPIROSE'}
                    for val in values:
                        if values[val] and val in [1, 2, 3]:
                            vacina = opcoes[val]

                    if data != '':
                        try:
                            data = datetime.strptime(data, '%d/%m/%Y')
                        except:
                            raise DateException
                    
                    window.Close()
                    return {'chip': chip, 'vacina': vacina, 'data': data}

                except ChipException:
                    sg.popup('Chip invalido, por favor digite novamente.')
                except DateException:
                    sg.popup('Por favor, insira uma data de vacina válida.')
    
    def mostrar_mensagem(self, mensagem):
        if isinstance(mensagem, str):
            sg.popup(mensagem)