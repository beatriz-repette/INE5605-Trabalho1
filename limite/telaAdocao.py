from exception.chipException import ChipException
from limite.telaAbstrata import TelaAbstrata
from datetime import date, datetime
from verificacao import verificaCPF, verificaChip, verificaData
from exception.CPFexception import CPFExecption
from exception.dateException import DateException
import PySimpleGUI as sg


class TelaAdocao(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGreen')
        layout = [
            [sg.Text("-------- Adocao ----------", font=("Times",25,"bold"))],
            [sg.Text('Escolha sua opção:', font=("Times",15))],
            [sg.Radio('Registrar Adocao', "RD1", key=1)],
            [sg.Radio('Alterar Adocao', "RD1", key=2)],
            [sg.Radio('Listar Adocoes', "RD1", key=3)],
            [sg.Radio('Excluir Adocao', "RD1", key=4)],
            [sg.Radio('Relatorio de Adocoes', "RD1", key=5)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Cadastro de Adocao', layout)

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
        try:
            return opcao
        except UnboundLocalError:
            return 0

    def pega_dados_adocao(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("-------- Dados Adocao ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do adotante:", font=("Times",15))],
            [sg.Text("CPF:"), sg.InputText(key = 'cpf')],
            [sg.Text("Chip do animal:"), sg.InputText(key = 'animal')], #Precisa ser inteiro e maior que zero
            [sg.Text("Data:"), sg.Input(enable_events=True, key='data'), sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Checkbox("Assinou termo?", key = "assinou_termo")],
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
                cpf = (values['cpf']).replace(".", "").replace("-", "").strip()
                animal = values['animal']
                assinou_termo = values["assinou_termo"]


                try:
                    data = datetime.strptime(values['data'], "%d/%m/%Y")

                    verificaData(data)
                    verificaCPF(cpf)
                    verificaChip(animal)
                    #Add verifica data depois

                    self.__window.Close()
                    return {"data": data, "animal": animal, "cpf": cpf, "assinou_termo": assinou_termo}

                except CPFExecption:
                    sg.popup("O CPF digitado está incorreto, por favor o digite novamente.")
                except ChipException:
                    sg.popup("O valor de chip do animal inserido esta incorreto\n"
                             "Lembre que esse valor deve ser um inteiro positivo.")
                except (UnboundLocalError, ValueError): #Para caso existam campos nao preenchidos
                    sg.popup("Lembre-se de preencher todos os campos!")

    def pega_dados_alterados_adocao(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("-------- Alteracao de Adocao ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do adotante:", font=("Times", 15))],
            [sg.Text("CPF:"), sg.InputText(key='cpf')],
            [sg.Text("Chip do animal:"), sg.InputText(key='animal')],  # Precisa ser inteiro e maior que zero
            [sg.Text("Data:"), sg.Input(enable_events=True, key='data'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Checkbox("Assinou termo?", key="assinou_termo")],
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
                cpf = (values['cpf']).replace(".", "").replace("-", "").strip()
                animal = values['animal']
                assinou_termo = values["assinou_termo"]

                try:
                    data = datetime.strptime(values['data'], "%d/%m/%Y")

                    verificaData(data)
                    verificaCPF(cpf)
                    verificaChip(animal)

                    self.__window.Close()
                    return {"data": data, "animal": animal, "cpf": cpf, "assinou_termo": assinou_termo}

                except CPFExecption:
                    sg.popup("O CPF digitado está incorreto, por favor o digite novamente.")
                except ChipException:
                    sg.popup("O valor de chip do animal inserido esta incorreto\n"
                             "Lembre que esse valor deve ser um inteiro positivo.")
                except DateException:
                    sg.popup("A data inserida esta no futuro.\n"
                             "Por favor, insira uma data valida")
                except (UnboundLocalError, ValueError):  # Para caso existam campos nao preenchidos
                    sg.popup("Lembre-se de preencher todos os campos!")

    def seleciona_adocao(self, len): #Ver se isso vai funcionar
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("Posicao da adocao na database:"), sg.InputText(key='adocao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                self.__window.Close()
                return 0

            if event == "Confirmar":
                cpf = (values['cpf']).replace(".", "").replace("-", "").strip()

                try:
                    adocao = int(adocao)
                    if adocao < 0 or adocao >= len:
                        raise ValueError
                    self.__window.Close()
                    return adocao
                except ValueError:
                    sg.popup("Por favor, insira uma posicao valida.")

    def seleciona_periodo(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("------ Relatorio de Adocoes --------", font=("Times", 25, "bold"))],
            [sg.Text("Relatorio de adocoes por periodo.", font=("Times", 15))],
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
                    data_inicio = datetime.strptime(values['data'], "%d/%m/%Y")
                    data_fim = datetime.strptime(values['data'], "%d/%m/%Y")

                    verificaData(data_inicio)
                    verificaData(data_fim)

                    self.__window.Close()
                    return {'inicio': data_inicio, 'fim': data_fim}

                except DateException:
                    sg.popup("A data inserida esta no futuro.\n"
                             "Por favor, insira uma data valida")
                except (UnboundLocalError, ValueError):  # Para caso existam campos nao preenchidos
                    sg.popup("Lembre-se de preencher todos os campos!")

    def mostrar_adocao(self, dados):

        dados_tabela = []
        for i, dados in enumerate(dados, start=1):
            linha = [
                i,
                dados["animal"],
                dados["data"].strftime("%d/%m/%Y"),
                dados["chip"],
                dados["cpf"],
                "SIM" if dados["assinou_termo"] else "NÃO"
            ]
            dados_tabela.append(linha)

        cabecalho = ["Numero Adocao", "Animal", "Data da Adocao", "Numero do Chip", "CPF do Adotante", "Assinou o termo de responsabilidade?"]

        layout = [
            [sg.Text("Adoções Registradas")],
            [sg.Table(values=dados_tabela, headings=cabecalho, auto_size_columns=False, justification='center',
                      num_rows=10, key="-TABELA-")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Adoções", layout)

        while True:
            evento, valores = window.read()
            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                break

        window.close()
