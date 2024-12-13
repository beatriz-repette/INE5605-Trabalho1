from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
from verificacao import verificaNome
from exception.erroCadastroException import ErroCadastroException
from exception.chipException import ChipException
from exception.dateException import DateException
import PySimpleGUI as sg


class TelaGato(TelaAbstrata):
    def tela_opcoes(self):
        layout = [
        [sg.Text("-------- ONG de Animais ---------", font=("Times",25,"bold"))],
        [sg.Text('Escolha sua opção:', font=("Times",15))],
        [sg.Radio('Ver gatos', "RADIO1", key = 1, default = True, size=(10
        ,1))],
        [sg.Radio('Adicionar vacina', "RADIO1", key = 2)],
        [sg.Radio('Alterar gato', "RADIO1", key = 3)],
        [sg.Radio('Excluir gato', "RADIO1", key = 4)],
        [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Gatos').Layout(layout)
        button, values = window.Read()
        opcao = 0
        if button != 'Cancel':
            for val in values:
                if values[val]:
                    opcao = val
        window.close()
        return opcao
    
    def pegar_dados_gato(self):
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
            [sg.Text("-------- Dados Gato ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do gato:", font=("Times",15))],
            [sg.Text("Nome do gato:"), sg.InputText(key = 'nome')],
            [sg.Text("Chip do gato:"), sg.InputText(key = 'chip')],
            [sg.Text("Raca do gato:"), sg.InputText(key = 'raca')],
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
                nome = values['nome']
                chip = values['chip']
                raca = values['raca']

                gato = {}
                try:
                    # Verificacao de nome
                    if nome == '':
                        nome = '*'
                    else:
                        verificaNome(nome)
                    gato.update({'nome': nome})

                    if chip == '':
                        chip = '*'
                    else:
                        chip = int(chip)
                        if chip < 0:
                            raise ChipException
                    gato.update({'chip': chip})

                    if raca == '':
                        raca = '*'
                    gato.update({'raca': raca})

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
                    gato.update({'vacinas': vacinas_animal})
                    window.close()
                    return gato
                
                except ErroCadastroException:
                    sg.popup("Nome invalido, por favor digite novamente.")
                except ChipException:
                    sg.popup('Chip invalido, por favor digite novamente.')
                except DateException:
                    sg.popup('Por favor, insira uma data de vacina válida.')

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
                except ChipException:
                    sg.popup('Chip invalido, por favor digite novamente.')
                except DateException:
                    sg.popup('Por favor, insira uma data de vacina válida.')

    def mostrar_gato(self, dados):
        '''
        print('--------' + ' Gato: ' + dados['animal'] + ' ----------')
        print('Numero do chip: ' + str(dados['chip']))
        print('Raca: ' + dados['raca'])
        print('Vacinas:', dados['vacinas'])
        print('Foi adotado:', 'Sim' if dados['adotado'] else 'Nao')
        '''

        layout = [
            [sg.Text("Lista de Gatos", font=("Times", 25, "bold"))],
            [sg.Table(values=dados,
                      headings=["Nome", "Chip", "Raca", "Vacinas", "Foi adotado"],
                      auto_size_columns=True,
                      justification='center',
                      num_rows=10,
                      key='-TABELA-')],
            [sg.Button("Fechar")]
        ]

        # Criar janela para exibir a tabela
        window = sg.Window("Gatos", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()

    def seleciona_gato(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("Chip do gato que deseja selecionar:"), sg.InputText(key='chip')],
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

    def mensagem_sem_gatos(self):
        sg.popup("Nao existem gatos cadastrados no sistema.", title="Cancelado")

    def mensagem_erro_vacina(self):
        sg.popup('Erro ao adicionar vacinas.')

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)
