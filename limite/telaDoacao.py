from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
from verificacao import verificaCPF, verificaData, verificaChip, verificaNome
from exception.CPFexception import CPFExecption
from verificacao import verificaNome
from exception.erroCadastroException import ErroCadastroException
from exception.dateException import DateException
from exception.chipException import ChipException
from exception.nomeException import NomeException
import PySimpleGUI as sg


class TelaDoacao(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGreen')
        layout = [
            [sg.Text("-------- Doacao ----------", font=("Times", 25, "bold"))],
            [sg.Text('Escolha sua opção:', font=("Times", 15))],
            [sg.Radio('Registrar Doacao', "RD1", default = True, key=1)],
            [sg.Radio('Alterar Doacao', "RD1", key=2)],
            [sg.Radio('Listar Doacoes', "RD1", key=3)],
            [sg.Radio('Excluir Doacao', "RD1", key=4)],
            [sg.Radio('Relatorio de Doacoes', "RD1", key=5)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Cadastro de Doação', layout)

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.read()

        if button in (None, 'Cancelar'):
            opcao = 0

        else:
            for val in values:
                if values[val]:
                    opcao = val

        self.__window.Close()
        try:
            return opcao
        except UnboundLocalError:
            return 0

    def pega_dados_doacao(self):
        sg.ChangeLookAndFeel('DarkGreen')
        visivel1 = False
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
            [sg.Text("-------- Dados Doacao ----------", font=("Times", 25, "bold"))],
            [sg.Text("CPF do doador:"), sg.InputText(key='cpf')],
            [sg.Text("Data da doacao:"), sg.Input(enable_events=True, key='data'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Text("Preencha os seguintes campos referentes ao animal:", font=("Times", 15))],
            [sg.Text("Tipo:")],
            [sg.Radio("Cachorro", "TIPO_ANIMAL", key="cachorro"), sg.Radio("Gato", "TIPO_ANIMAL", key="gato")],
            [sg.Text("Tamanho (o tamanho so precisa ser preenchido caso o animal for um cachorro):"),
             sg.Combo(["P", "M", "G"], key="TAMANHO")],
            [sg.Text("Numero do chip:"), sg.InputText(key='chip')],
            [sg.Text("Nome:"), sg.InputText(key='nome')],
            [sg.Text("Raca:"), sg.InputText(key='raca')],
            [sg.Text("Vacinas:")],
            [sg.Checkbox('Raiva',enable_events = True, key = 'raiva'),
             self.collapse(vac_raiva, 'sec-raiva', False)],
            [sg.Checkbox('Hepatite', enable_events = True, key = 'hepatite'),
             self.collapse(vac_hep, 'sec-hepatite', False)],
            [sg.Checkbox('Leptospirose', enable_events = True, key = 'lepto'),
             self.collapse(vac_lepto, 'sec-lepto', False)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Cadastro de Doação', layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                self.__window.Close()
                return 0
            
            if event == 'raiva':
                visivel1 = not visivel1
                self.__window['sec-raiva'].update(visible = visivel1)

            if event == 'hepatite':
                visivel2 = not visivel2
                self.__window['sec-hepatite'].update(visible = visivel2)

            if event == 'lepto':
                visivel3 = not visivel3
                self.__window['sec-lepto'].update(visible = visivel3)

            if event == "Confirmar":
                try:
                    cpf = (values['cpf']).replace(".", "").replace("-", "").strip()
                    data = datetime.strptime(values['data'], '%d/%m/%Y')
                    tipo_animal = "cachorro" if values["cachorro"] else "gato"
                    tamanho = values['TAMANHO'] if tipo_animal == 'cachorro' else None
                    chip = values['chip']
                    nome = values['nome']
                    raca = values['raca']

                    chip = int(chip)
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

                    if visivel1:
                        vacinas_animal.append({'data': data_vacina_rai, 'nome': 1, 'animal': chip})
                    elif visivel2:
                        vacinas_animal.append({'data': data_vacina_hep, 'nome': 2, 'animal': chip})
                    elif visivel3:
                        vacinas_animal.append({'data': data_vacina_lep, 'nome': 3, 'animal': chip})

                    # Verificacoes
                    verificaData(data)
                    verificaCPF(cpf)
                    verificaNome(nome)

                    if tipo_animal == 'cachorro':
                        animal = {
                            'tipo': tipo_animal,
                            'tamanho': tamanho,
                            'chip': chip,
                            'nome': nome,
                            'raca': raca,
                            'vacinas': vacinas_animal
                        }

                    else:
                        animal = {
                            'tipo': tipo_animal,
                            'chip': chip,
                            'nome': nome,
                            'raca': raca,
                            'vacinas': vacinas_animal
                        }

                    motivo = sg.popup_get_text("Qual o motivo da doação?", "Motivo")
                    if not motivo:
                        sg.popup("Motivo da doação não pode ser vazio!")
                        continue

                    self.__window.Close()
                    return {"data": data, "animal": animal, "cpf": cpf, "motivo": motivo}

                except CPFExecption:
                    sg.popup("O CPF digitado está incorreto, por favor o digite novamente.")
                except DateException:
                    sg.popup("A data inserida esta no futuro.\n"
                             "Por favor, insira uma data valida")
                except NomeException:
                    sg.popup("O nome do animal inserido nao eh valido. \nPor favor, use apenas letras e espacos.")
                except ChipException:
                    sg.popup("O valor de chip do animal inserido esta incorreto\n"
                             "Lembre que esse valor deve ser um inteiro positivo.")
                except (UnboundLocalError, ValueError):  # Para caso existam campos nao preenchidos
                    sg.popup("Lembre-se de preencher todos os campos!")
                except:
                    sg.popup('Erro ao registrar doacao.')

    def pega_dados_alterados_doacao(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("-------- Alteracao de Doacao ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados da Doacao:", font=("Times", 15))],
            [sg.Text("CPF do doador:"), sg.InputText(key='cpf')],
            [sg.Text("Data:"), sg.Input(enable_events=True, key='data'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Text("Motivo"), sg.InputText(key="motivo")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Menu').Layout(layout)

        #######
        while True:
            event, values = self.__window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                self.__window.Close()
                return 0

            if event == "Confirmar":
                cpf = values['cpf']
                motivo = values["motivo"]
                data = values['data']

                try:
                    if data != '':
                        data = datetime.strptime(values['data'], "%d/%m/%Y")
                        verificaData(data)
                    if cpf != '':
                        cpf = cpf.replace(".", "").replace("-", "").strip()
                        verificaCPF(cpf)

                    self.__window.Close()
                    return {"data": data, "cpf": cpf, "motivo": motivo}

                except CPFExecption:
                    sg.popup("O CPF digitado está incorreto, por favor o digite novamente.")
                except ChipException:
                    sg.popup("O valor de chip do animal inserido esta incorreto\n"
                             "Lembre que esse valor deve ser um inteiro positivo.")
                except DateException:
                    sg.popup("A data inserida esta no futuro.\n"
                             "Por favor, insira uma data valida")

    def mostrar_doacao(self, dados):
        dados_tabela = []
        for d in dados:
            linha = [
                d['n'],
                d["animal"],
                d["data"],
                d["chip"],
                d["cpf"],
                d['motivo']
            ]
            dados_tabela.append(linha)

        cabecalho = ["Numero Doacao", "Animal", "Data da Doacao", "Numero do Chip", "CPF do Doador", "Motivo"]

        layout = [
            [sg.Text("Doacoes Registradas")],
            [sg.Table(values=dados_tabela, headings=cabecalho, auto_size_columns=True, justification='center',
                      num_rows=10, key="-TABELA-")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Doacoes", layout)

        while True:
            evento, valores = window.read()
            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                break

        window.close()

    def seleciona_doacao(self, len):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("Posicao da doacao na database:"), sg.InputText(key='doacao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                self.__window.Close()
                return 0

            if event == "Confirmar":

                try:
                    doacao = int(values['doacao'])
                    if doacao <= 0 or doacao > len:
                        raise ValueError
                    self.__window.Close()
                    return doacao
                except ValueError:
                    sg.popup("Por favor, insira uma posicao valida.")

    def seleciona_periodo(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("------ Relatorio de Doacoes --------", font=("Times", 25, "bold"))],
            [sg.Text("Relatorio de doacoes por periodo.", font=("Times", 15))],
            [sg.Text("Selecione o periodo a ser consultado:", font=("Times", 15))],
            [sg.Text("Data inicial:"), sg.Input(enable_events=True, key='data_inicio'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Text("Data final:"), sg.Input(enable_events=True, key='data_fim'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                self.__window.Close()
                return 0

            if event == "Confirmar":
                try:
                    data_inicio = datetime.strptime(values['data_inicio'], "%d/%m/%Y")
                    data_fim = datetime.strptime(values['data_fim'], "%d/%m/%Y")

                    verificaData(data_inicio)
                    verificaData(data_fim)

                    self.__window.Close()
                    return {'inicio': data_inicio, 'fim': data_fim}

                except DateException:
                    sg.popup("A data inserida esta no futuro.\n"
                             "Por favor, insira uma data valida")
                except (UnboundLocalError, ValueError):  # Para caso existam campos nao preenchidos
                    sg.popup("Lembre-se de preencher todos os campos!")

