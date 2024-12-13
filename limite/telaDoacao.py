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
            [sg.Radio('Registrar Doacao', "RD1", key=1)],
            [sg.Radio('Alterar Doacao', "RD1", key=2)],
            [sg.Radio('Listar Doacoes', "RD1", key=3)],
            [sg.Radio('Excluir Doacao', "RD1", key=4)],
            [sg.Radio('Relatorio de Doacoes', "RD1", key=4)],
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

        layout = [
            [sg.Text("-------- Dados Doacao ----------", font=("Times", 25, "bold"))],
            [sg.Text("CPF do doador:"), sg.InputText(key='cpf')],
            [sg.Text("Data da doacao:"), sg.Input(enable_events=True, key='data'),
             sg.CalendarButton("Selecionar Data", target="data", format="%d/%m/%Y")],
            [sg.Text("Preencha os seguintes campos referentes ao animal?", font=("Times", 15))],
            [sg.Text("Tipo:")],
            [sg.Radio("Cachorro", "TIPO_ANIMAL", key="cachorro"), sg.Radio("Gato", "TIPO_ANIMAL", key="gato")],
            [sg.Text("Tamanho (o tamanho so precisa ser preenchido caso o animal for um cachorro):"),
             sg.Combo(["P", "M", "G"], key="TAMANHO")],
            [sg.Text("Numero do chip:"), sg.InputText(key='chip')],
            [sg.Text("Nome:"), sg.InputText(key='nome')],
            [sg.Text("Raca:"), sg.InputText(key='raca')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Cadastro de Doação', layout)

        vacinas = []

        while True:
            event, values = self.__window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                self.__window.Close()
                return 0

            if event == "Confirmar":
                try:
                    cpf = (values['cpf']).replace(".", "").replace("-", "").strip()
                    data = datetime.strptime(values['data'], '%d/%m/%Y')
                    tipo_animal = "cachorro" if values["cachorro"] else "gato"
                    tamanho = values['TAMANHO'] if tipo_animal == 'cachorro' else None
                    chip = values['chip']
                    nome = values['nome']
                    raca = values['raca']

                    if tipo_animal == 'cachorro':
                        animal = {
                            'tipo': tipo_animal,
                            'tamanho': tamanho,
                            'chip': chip,
                            'nome': nome,
                            'vacina': None,
                            'raca': raca,
                        }

                    else:
                        animal = {
                            'tipo': tipo_animal,
                            'chip': chip,
                            'nome': nome,
                            'raca': raca,
                            'vacina': None
                        }

                    motivo = sg.popup_get_text("Qual o motivo da doação?", "Motivo")
                    if not motivo:
                        sg.popup("Motivo da doação não pode ser vazio!")
                        continue

                    # Verificacoes
                    verificaData(data)
                    verificaCPF(cpf)
                    verificaChip(chip)
                    verificaNome(nome)

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

    def pega_dados_alterados_doacao(self):
        print("-------- Alteracao de Doacao (insira 0 para cancelar ou * para avancar) ----------")
        cpf = input("CPF: ").replace(".", "").replace("-", "").strip()
        while True:
            if cpf == '0':
                return 0
            elif cpf == '*':
                break
            try:
                verificaCPF(cpf)
                break
            except (CPFExecption, ValueError):
                print("O CPF digitado está incorreto, por favor o digite novamente.")
                cpf = input("CPF: ").replace(".", "").replace("-", "").strip()

        data = input("Data (formato DD/MM/YYYY): ")
        while True:
            if data == '0':
                return 0
            elif data == '*':
                break
            try:
                data = datetime.strptime(data, '%d/%m/%Y')
                break
            except:
                print('Data invalida inserida.')
                data = input("Data (formato DD/MM/YYYY): ")

        chip_animal = input('Numero do chip do animal: ')
        while True:
            if chip_animal == '0':
                return 0
            elif chip_animal == '*':
                break
            try:
                chip_animal = int(chip_animal)
                if chip_animal < 0:
                    raise ValueError
                break
            except:
                print('Valor de chip invalido.')
                chip_animal = input('Numero do chip do animal: ')

        motivo = input("Qual o motivo da doacao? ")
        if motivo == '0':
            return 0

        return {"data": data, "chip": chip_animal, "cpf": cpf, "motivo": motivo}

    def mostrar_doacao(self, dados, n):
        print('-------- Doacao:', n, '----------')
        print('Animal: ' + dados['animal'])
        print('Data da doacao: ' + dados['data'].strftime('%d/%m/%Y'))
        print('Numero do chip: ' + str(dados['chip']))
        print('CPF do doador: ' + dados['cpf'])
        print('Motivo da doacao: ' + dados['motivo'])

    def seleciona_doacao(self, len):
        doacao = input("Posicao da doacao na database (Digite * para retornar): ")
        while True:
            if doacao == '*':
                break
            try:
                doacao = int(doacao)
                if doacao < 0 or doacao >= len:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, insira uma posicao valida.")
                doacao = input("Posicao da doacao na database (Digite * para retornar): ")
        return doacao

    def seleciona_periodo(self):
        print('-------- Relatorio de Doacoes --------')
        data_inicial = input("Inicio do periodo (formato DD/MM/YYYY): ")
        while True:
            if data_inicial == '0':
                return 0
            try:
                data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
                break
            except:
                print('Data invalida inserida.')
                data_inicial = input("Inicio do periodo (formato DD/MM/YYYY): ")
        data_final = input("Fim do periodo (formato DD/MM/YYYY): ")
        while True:
            if data_final == '0':
                return 0
            try:
                data_final = datetime.strptime(data_final, '%d/%m/%Y')
                break
            except:
                print('Data invalida inserida.')
                data_final = input("Fim do periodo (formato DD/MM/YYYY): ")
        return {'inicio': data_inicial, 'fim': data_final}

