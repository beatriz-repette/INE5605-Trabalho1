from verificacao import verificaCPF, verificaNome, verificaEndereco, verificaData
from limite.telaAbstrata import TelaAbstrata
from exception.CPFexception import CPFExecption
from exception.dateException import DateException
from exception.erroCadastroException import ErroCadastroException
from datetime import datetime
import PySimpleGUI as sg
from exception.nomeException import NomeException
from exception.enderecoException import EnderecoException

class TelaDoador(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGreen')
        layout = [
            [sg.Text("-------- Doador ----------", font=("Times",25,"bold"))],
            [sg.Text('Escolha sua opção:', font=("Times",15))],
            [sg.Radio('Incluir Doador', "RD1", default = True, key=1)],
            [sg.Radio('Alterar Doador', "RD1", key=2)],
            [sg.Radio('Listar Doadores', "RD1", key=3)],
            [sg.Radio('Excluir Doador', "RD1", key=4)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Menu').Layout(layout)

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

    def pega_dados_doador(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("-------- Dados Doador ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do doador:", font=("Times", 15))],
            [sg.Text("CPF:"), sg.InputText(key='cpf')],
            [sg.Text("Nome:"), sg.InputText(key='nome')],
            [sg.Text("Data de nascimento:"), sg.Input(enable_events=True, key='data'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Text("Endereco:"), sg.InputText(key='endereco')],
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
                nome = values['nome']
                endereco = values['endereco']

                try:
                    data = datetime.strptime(values['data'], "%d/%m/%Y")

                    verificaCPF(cpf)
                    verificaNome(nome)
                    verificaEndereco(endereco)
                    verificaData(data)

                    self.__window.Close()
                    return {"nome": nome, "endereco": endereco, "data_nascimento": data, "cpf": cpf}

                except CPFExecption:
                    sg.popup("O CPF digitado está incorreto, por favor o digite novamente.")
                except DateException:
                    sg.popup("A data inserida esta no futuro.\n"
                             "Por favor, insira uma data valida")
                except NomeException:
                    sg.popup("Nome invalido, por favor digite novamente."
                             "\nLembre de inserir seu nome completo.") #Ver como pular a linha dentro do popup!!
                except EnderecoException:
                    sg.popup("Endereco invalido, por favor digite novamente."
                             "\nLembre de escrever ao menos sua cidade, rua e numero!")
                except (UnboundLocalError, ValueError):  # Para caso existam campos nao preenchidos
                    sg.popup("Lembre-se de preencher todos os campos!")

    def seleciona_doador(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("CPF do doador que deseja selecionar:"), sg.InputText(key='cpf')],
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
                    verificaCPF(cpf)
                    self.__window.Close()
                    return cpf

                except CPFExecption:
                    sg.popup("O CPF digitado está incorreto, por favor o digite novamente.")

    def pega_dados_alterados_doador(self): #igual o anterior, mas sem a opcao de cpf
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("-------- Dados Doador ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do doador:", font=("Times", 15))],
            [sg.Text("CPF:"), sg.InputText(key='cpf')],
            [sg.Text("Nome:"), sg.InputText(key='nome')],
            [sg.Text("Data de nascimento:"), sg.Input(enable_events=True, key='data'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Text("Endereco:"), sg.InputText(key='endereco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Menu').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                self.__window.Close()
                return 0


            if event == "Confirmar":
                nome = values['nome']
                endereco = values['endereco']
                cpf = values['cpf']
                data = values['data']

                try:
                    if cpf != '':
                        cpf = (cpf).replace(".", "").replace("-", "").strip()
                        verificaNome(nome)
                    if data != '':
                        data = datetime.strptime(data, "%d/%m/%Y")
                        verificaData(data)
                    if endereco != '':
                        verificaEndereco(endereco)
                    
                    self.__window.Close()
                    return {"nome": nome, "endereco": endereco, "data_nascimento": data,
                           'cpf': cpf}

                except NomeException:
                    sg.popup("Nome invalido, por favor digite novamente."
                             "\nLembre de inserir seu nome completo.")
                except DateException:
                    sg.popup("A data inserida esta no futuro.\n"
                             "Por favor, insira uma data valida")
                except EnderecoException:
                    sg.popup("Endereco invalido, por favor digite novamente."
                             "\nLembre de escrever ao menos sua cidade, rua e numero!")
                except (ValueError):
                    sg.popup("Erro ao alterar doacao.")
                except CPFExecption:
                    sg.popup("O CPF digitado está incorreto, por favor o digite novamente.")

    def mostra_doador(self, dados_doador):
        layout = [
            [sg.Text("Lista de Doadores", font=("Times", 25, "bold"))],
            [sg.Table(values=dados_doador,
                      headings=["Nome", "Endereço", "CPF", "Data de Nascimento"],
                      auto_size_columns=True,
                      justification='center',
                      num_rows=10,
                      key='-TABELA-')],
            [sg.Button("Fechar")]
        ]

        # Criar janela para exibir a tabela
        window = sg.Window("Doadores", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()