from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
from verificacao import verificaNome
from exception.erroCadastroException import ErroCadastroException
from exception.chipException import ChipException
from exception.tamanhoException import TamanhoException
from exception.dateException import DateException
import PySimpleGUI as sg


class TelaCachorro(TelaAbstrata):
    def tela_opcoes(self):
        layout = [
        [sg.Text("-------- ONG de Animais ---------", font=("Times",25,"bold"))],
        [sg.Text('Escolha sua opção:', font=("Times",15))],
        [sg.Radio('Ver cachorros', "RADIO1", key = 1, default = True, size=(10
        ,1))],
        [sg.Radio('Adicionar vacina', "RADIO1", key = 2)],
        [sg.Radio('Alterar cachorros', "RADIO1", key = 3)],
        [sg.Radio('Excluir cachorros', "RADIO1", key = 4)],
        [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Cachorros').Layout(layout)
        button, values = window.Read()
        opcao = 0
        if button != 'Cancel':
            for val in values:
                if values[val]:
                    opcao = val
        window.close()
        return opcao
    
    def seleciona_cachorro(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("Chip do cachorro que deseja selecionar:"), sg.InputText(key='chip')],
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

    def mostrar_cachorro(self, dados):
        '''
        print('--------' + ' Cachorro: ' + dados['animal'] + ' ----------')
        print('Numero do chip: ' + str(dados['chip']))
        print('Tamanho: ' + dados['tamanho'])
        print('Raca: ' + dados['raca'])
        print('Vacinas:', dados['vacinas'])
        print('Foi adotado:', 'Sim' if dados['adotado'] else 'Nao')
        '''

        layout = [
            [sg.Text("Lista de Cachorros", font=("Times", 25, "bold"))],
            [sg.Table(values=dados,
                      headings=["Nome", "Chip", "Tamanho", "Raca", "Vacinas", "Foi adotado"],
                      auto_size_columns=True,
                      justification='center',
                      num_rows=10,
                      key='-TABELA-')],
            [sg.Button("Fechar")]
        ]

        # Criar janela para exibir a tabela
        window = sg.Window("Cachorros", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()
        
    def mensagem_sem_cachorros(self):
        sg.popup("Nao existem cachorros cadastrados no sistema")

    def mensagem_erro_vacina(self):
        sg.popup('Erro ao adicionar vacinas.')

    def pegar_dados_cachorro(self):
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
            [sg.Text("-------- Dados cachorro ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do cachorro:", font=("Times",15))],
            [sg.Text("Nome do cachorro:"), sg.InputText(key = 'nome')],
            [sg.Text("Chip do cachorro:"), sg.InputText(key = 'chip')],
            [sg.Text("Tamanho do cachorro:"), sg.InputText(key = 'tamanho')],
            [sg.Text("Raca do cachorro:"), sg.InputText(key = 'raca')],
            [sg.Text("Vacinas:")],
            [sg.Checkbox('Raiva',enable_events = True, key = 'raiva'),
             self.collapse(vac_raiva, 'sec-raiva', False)],
            [sg.Checkbox('Hepatite', enable_events = True, key = 'hepatite'),
             self.collapse(vac_hep, 'sec-hepatite', False)],
            [sg.Checkbox('Leptospirose', enable_events = True, key = 'lepto'),
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
                tamanho = values['tamanho']
                raca = values['raca']
                
        
                cachorro = {}
                try:
                    # Verificacao de nome
                    if nome == '':
                        nome = '*'
                    else:
                        verificaNome(nome)
                    cachorro.update({'nome': nome})

                    if chip == '':
                        chip = '*'
                    else:
                        chip = int(chip)
                        if chip < 0:
                            raise ChipException
                    cachorro.update({'chip': chip})

                    if tamanho == '':
                        tamanho = '*'
                    else:
                        tamanho = tamanho.upper()
                        if tamanho not in ['P', 'M', 'G']:
                            raise TamanhoException
                    cachorro.update({'tamanho': tamanho})

                    if raca == '':
                        raca = '*'
                    cachorro.update({'raca': raca})

                    vacinas_animal = []

                    data_vacina_rai = values['data-raiva']
                    # Se raiva não estiver marcado, desconsidera o texto armazenado
                    if not visivel1:
                        data_vacina_rai = ''
                    if data_vacina_rai != '':
                        try:
                            data_vacina_rai = datetime.strptime(data_vacina_rai, '%d/%m/%Y')
                        except:
                            raise DateException

                    data_vacina_hep = values['data-hepatite']
                    # Se hepatite não estiver marcado, desconsidera o texto armazenado
                    if not visivel2:
                        data_vacina_hep = ''
                    if data_vacina_hep != '':
                        try:
                            data_vacina_hep = datetime.strptime(data_vacina_hep, '%d/%m/%Y')
                        except:
                            raise DateException

                    data_vacina_lep = values['data-lepto']
                    # Se lepto não estiver marcado, desconsidera o texto armazenado
                    if not visivel3:
                        data_vacina_lep = ''
                    if data_vacina_lep != '':
                        try:
                            data_vacina_lep = datetime.strptime(data_vacina_lep, '%d/%m/%Y')
                        except:
                            raise DateException

                    if (visivel1 or visivel2 or visivel3):
                        vacinas_animal.append({'data': data_vacina_rai, 'nome': 1, 'animal': chip})
                        vacinas_animal.append({'data': data_vacina_hep, 'nome': 2, 'animal': chip})
                        vacinas_animal.append({'data': data_vacina_lep, 'nome': 3, 'animal': chip})
                    else:
                        vacinas_animal = '*'

                    cachorro.update({'vacinas': vacinas_animal})
                    window.close()
                    return cachorro

                except ErroCadastroException:
                    sg.popup("Nome invalido, por favor digite novamente.")
                except ChipException:
                    sg.popup('Chip invalido, por favor digite novamente.')
                except TamanhoException:
                    sg.popup('Por favor, insira um tamanho valido.')
                except DateException:
                    sg.popup('Por favor, insira uma data de vacina válida.')

    def pegar_vacina(self, chip):
        sg.ChangeLookAndFeel('DarkGreen')
        visivel1 = True
        visivel2 = False
        visivel3 = False

        vac_raiva = [[sg.Text('Data de aplicacao:'),
                      sg.Input(key = 'data-raiva'),
                      sg.CalendarButton("Selecionar Data", target="data-raiva", format="%d/%m/%Y")]]
        
        vac_hep = [[sg.Text('Data de aplicacao:'),
                    sg.Input(key = 'data-hepatite'),
                    sg.CalendarButton("Selecionar Data", target="data-hepatite", format="%d/%m/%Y")]]
        
        vac_lepto = [[sg.Text('Data de aplicacao:'),
                      sg.Input(key = 'data-lepto'),
                      sg.CalendarButton("Selecionar Data", target="data-lepto", format="%d/%m/%Y")]]

        layout = [
            [sg.Text("-------- Dados Vacina ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados da vacina:", font=("Times",15))],
            [sg.Radio("Vacina da raiva", 'VACINAS', default = True, enable_events = True, key = 'raiva'),
             self.collapse(vac_raiva, 'sec-raiva', True)],
            [sg.Radio("Vacina da hepatite", 'VACINAS', enable_events = True, key = 'hepatite'),
             self.collapse(vac_hep, 'sec-hepatite', False)],
            [sg.Radio("Vacina da leptospirose", 'VACINAS', enable_events = True, key = 'lepto'),
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
                visivel1 = True
                visivel2 = False
                visivel3 = False
                window['sec-raiva'].update(visible = visivel1)
                window['sec-hepatite'].update(visible = visivel2)
                window['sec-lepto'].update(visible = visivel3)

            if event == 'hepatite':
                visivel1 = False
                visivel2 = True
                visivel3 = False
                window['sec-raiva'].update(visible = visivel1)
                window['sec-hepatite'].update(visible = visivel2)
                window['sec-lepto'].update(visible = visivel3)

            if event == 'lepto':
                visivel1 = False
                visivel2 = False
                visivel3 = True
                window['sec-raiva'].update(visible = visivel1)
                window['sec-hepatite'].update(visible = visivel2)
                window['sec-lepto'].update(visible = visivel3)

            if event == "Confirmar":
                try:
                    data = ''
                    if visivel1:
                        data = values['data-raiva']
                        vac = 1
                    elif visivel2:
                        data = values['data-hepatite']
                        vac = 2
                    elif visivel3:
                        data = values['data-lepto']
                        vac = 3

                    if data != '':
                        try:
                            data = datetime.strptime(data, '%d/%m/%Y')
                        except:
                            raise DateException

                    if (visivel1 or visivel2 or visivel3):
                        vacina = {'data': data, 'nome': vac, 'animal': chip}

                    else:
                        vacina = '*'
                    window.close()
                    return vacina
                
                except ErroCadastroException:
                    sg.popup("Nome invalido, por favor digite novamente.")
                except ChipException:
                    sg.popup('Chip invalido, por favor digite novamente.')
                except DateException:
                    sg.popup('Por favor, insira uma data de vacina válida.')
    
    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)