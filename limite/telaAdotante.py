from verificacao import verificaCPF, verificaEndereco, verificaNome, verificaData
from exception.CPFexception import CPFExecption
from exception.enderecoException import EnderecoException
from exception.nomeException import NomeException
from exception.dateException import DateException
from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
import PySimpleGUI as sg


class TelaAdotante(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGreen')
        layout = [
            [sg.Text("-------- Adotante ----------", font=("Times",25,"bold"))],
            [sg.Text('Escolha sua opção:', font=("Times",15))],
            [sg.Radio('Incluir Adotante', "RD1", key=1)],
            [sg.Radio('Alterar Adotante', "RD1", key=2)],
            [sg.Radio('Listar Adotantes', "RD1", key=3)],
            [sg.Radio('Excluir Adotante', "RD1", key=4)],
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
        return opcao

    def pega_dados_adotante(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("-------- Dados Adotante ----------", font=("Times", 25, "bold"))],
            [sg.Text("Insira os dados do adotante:", font=("Times",15))],
            [sg.Text("CPF:"), sg.InputText(key = 'cpf')],
            [sg.Text("Nome:"), sg.InputText(key = 'nome')],
            [sg.Text("Data de nascimento:"), sg.Input(enable_events=True, key='data'), sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Text("Endereco:"), sg.InputText(key = 'endereco')],
            [sg.Text("Tipo de habitacao:")],
            [sg.Radio("Casa", "habitacao", key = 1),
             sg.Radio("Apartamento Pequeno", "habitacao", key = 2),
             sg.Radio("Apartamento Medio", "habitacao", key = 3),
             sg.Radio("Apartamento Grande", "habitacao", key = 4)],
            [sg.Checkbox("Possui um animal?", key = "possui_animal", tooltip="Marque se possui um animal")],
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
                possui_animal = values["possui_animal"]

                #Determinar tipo de habitacao
                for val in range(1, 5):
                    if values[val]:
                        tipo_habitacao = val

                try:
                    data = datetime.strptime(values['data'], "%d/%m/%Y")

                    verificaCPF(cpf)
                    verificaNome(nome)
                    verificaEndereco(endereco)
                    verificaData(data)

                    self.__window.Close()
                    return {"nome": nome, "endereco": endereco, "data_nascimento": data, "cpf": cpf,
                            "tipo_habitacao": tipo_habitacao, "possui_animal": possui_animal}

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
                except Exception: #Para caso existam campos nao preenchidos
                    sg.popup("Lembre-se de preencher todos os campos!")

    def seleciona_adotante(self):
        sg.ChangeLookAndFeel('DarkGreen')

        layout = [
            [sg.Text("CPF do adotante que deseja selecionar:"), sg.InputText(key='cpf')],
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

    def mostra_adotante(self, dados_adotante):

        layout = [
            [sg.Text("Lista de Adotantes", font=("Times", 25, "bold"))],
            [sg.Table(values=dados_adotante,
                      headings=["Nome", "Endereço", "CPF", "Data de Nascimento", "Tipo de Habitação", "Possui Animal"],
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