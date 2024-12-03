from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
from verificacao import verificaNome
from exception.erroCadastroException import ErroCadastroException
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

        layout = [
            [sg.Text("-------- Dados Gato ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do gato:", font=("Times",15))],
            [sg.Text("Nome do gato:"), sg.InputText(key = 'nome')],
            [sg.Text("Chip do gato:"), sg.InputText(key = 'chip')],
            [sg.Text("Raca do gato:"), sg.InputText(key = 'raca')],
            [sg.Checkbox("Vacina da raiva:", enable_events = True, key = 'raiva'), sg.Input(key = 'data-raiva', visible = False), sg.CalendarButton("Selecionar Data", target="data-raiva", format="%d/%m/%Y", visible = False, key = 'slc_rai')],
            [sg.Checkbox("Vacina da hepatite:", enable_events = True, key = 'hepatite'), sg.Input(key = 'data-hepatite', visible = False), sg.CalendarButton("Selecionar Data", target="data-hepatite", format="%d/%m/%Y", visible = False, key = 'slc_hep')],
            [sg.Checkbox("Vacina da leptospirose:", enable_events = True, key = 'lepto'), sg.Input(key = 'data-lepto', visible = False), sg.CalendarButton("Selecionar Data", target="data-lepto", format="%d/%m/%Y", visible = False, key = 'slc_lep')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                window.Close()
                return 0


            if event == "Confirmar":
                cpf = (values['cpf']).replace(".", "").replace("-", "").strip()
                nome = values['nome']
                endereco = values['endereco']
                possui_animal = values["possui_animal"]

                #Determinar tipo de habitacao
                for val in range(1, 5):
                    if values[val]:
                        tipo_habitacao = val

            if event == 'raiva':
                visivel1 = not visivel1
                values['data-raiva'].update(visible = visivel1)

            if event == 'hepatite':
                visivel2 = not visivel2
                values['data-hepatite'].update(visible = visivel2)
                
        
            gato = {}

            # Verificacao de nome
            nome = input("Nome do gato: ")
            while True:
                if nome == '0':
                    return 0
                elif nome == '*':
                    break
                try:
                    verificaNome(nome)
                    break
                except ErroCadastroException:
                    print("Nome invalido, por favor digite novamente.")
                    nome = input("Nome: ")
            gato.update({'nome': nome})

            while True:
                try:
                    chip = input('Chip do gato: ')
                    if chip == '*':
                        break
                    chip = int(chip)
                    if chip < 0:
                        raise ValueError
                    break

                except ValueError:
                    print('Por favor, insira um chip valido.')
                    chip = input('Chip do gato: ')
            gato.update({'chip': chip})

            raca = input('Raca do gato: ')
            if raca == '0':
                return 0
            gato.update({'raca': raca})

            vacinas_animal = []
            while True:
                print("0 - Encerrar")
                print("1- Cadastrar nova vacina")
                print("* - Nao alterar vacinas")

                opcao = input('Opcao: ')
                while opcao not in ["1", "0", '*']:
                    opcao = input("Por favor, escolha uma opcao valida: ")
                if opcao == '0':
                    break
                elif opcao == '*':
                    vacinas_animal = '*'
                    break
                else:
                    print("Qual dessas vacinas voce quer cadastrar?")
                    print("0- Retornar")
                    print("1- Raiva")
                    print("2- Hepatite")
                    print("3- Leptospirose")

                    opcao2 = input('Vacina: ')
                    while opcao2 not in ['1', '2', '3', '0']:
                        print("Por favor, digite uma opcao valida: ")
                        opcao2 = input('Vacina: ')
                    if opcao2 == '0':
                        break
                    else:
                        data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
                        while True:
                            try:
                                data_vacina = datetime.strptime(data_vacina, '%d/%m/%Y')
                                break
                            except:
                                print("Por favor, digite uma data valida")
                                data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
                        
                vacinas_animal.append({'data': data_vacina, 'nome': int(opcao2), 'animal': chip})
            gato.update({'vacinas': vacinas_animal})
            window.close()
            return gato

    def pegar_vacina(self):
        print('-------------- Cadastro de Vacinas ---------------')
        vacinas_animal = []

        while True:
            try:
                chip_animal = input("Chip do animal: ")
                chip_animal = int(chip_animal)
                if chip_animal < 0:
                    raise ValueError
                break
            except:
                print('por favor, insira um chip valido.')
                chip_animal = input("Chip do animal: ")

        while True:
            print("0- Retornar")
            print("1- Cadastrar nova vacina")
            opcao = input()
            while opcao not in ["1", "0"]:
                opcao = input("Por favor, escolha uma opcao valida: ")
            if opcao == '0':
                break
            else:
                print("Qual dessas vacinas voce quer cadastrar?")
                print("0- Retornar")
                print("1- Raiva")
                print("2- Hepatite")
                print("3- Leptospirose")
                opcao2 = input('Vacina: ')
                while opcao2 not in ['1', '2', '3', '0']:
                    print("Por favor, digite uma opcao valida: ")
                    opcao2 = input('Vacina: ')
                if opcao2 == '0':
                    break
                else:
                    data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
                    while True:
                        try:
                            data_vacina = datetime.strptime(data_vacina, '%d/%m/%Y')
                            break
                        except:
                            print("Por favor, digite uma data valida")
                            data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
                    
            vacinas_animal.append({'data': data_vacina, 'nome': int(opcao2), 'animal': chip_animal})
        return vacinas_animal

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
        window = sg.Window("Adotantes", layout)

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
        print('Erro ao adicionar vacinas.')

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem)
