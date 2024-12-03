from exception.chipException import ChipException
from limite.telaAbstrata import TelaAbstrata
from datetime import date, datetime
from verificacao import verificaCPF, verificaChip
from exception.CPFexception import CPFExecption
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
            [sg.Radio('Relatorio de Adocoes', "RD1", key=4)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

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

        #DECIDIR COMO FAZER ISSO POR CAUSA DO DAO

        print("-------- Alteracao de Adocao (Insira 0 para retornar ou * para avancar) ----------")
        #Adicionar verificacao de tipo para cada um desses dados
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
                cpf = input("CPF: ")

        animal = input('Chip do animal: ')
        while True:
            if animal == '*':
                break
            try:
                animal = int(animal)
                if animal < 0:
                    raise Exception
                break
            except:
                print('ID invalido inserido.')
                animal = input('Chip do animal: ')

        data = input("Data (formato dia/mes/ano): ")
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
                data = input("Data (formato dia/mes/ano): ")

        assinou_termo = input("Assinou o termo de responsabilidade? (sim/nao): ")
        while True:
            if assinou_termo == '0':
                return 0
            elif assinou_termo == '*':
                break
            try:
                assinou_termo = assinou_termo.lower()
                if assinou_termo in ['sim', 'Sim']:
                    assinou_termo = True
                    break
                elif assinou_termo in ['nao', 'Nao']:
                    assinou_termo = False
                    break
                else:
                    raise Exception
            except:
                print('Insira uma opcao valida')
                assinou_termo = input("Assinou o termo de responsabilidade? (sim/nao): ")

        return {"data": data, "animal": animal, "cpf": cpf, "assinou_termo": assinou_termo}
    
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
        print('-------- Relatorio de Adocoes --------')
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

    def mostrar_adocao(self, dados, n):
        print('-------- Adocao:', n, '----------') #Pesquisar como botar esse "n" na interface
        print('Animal: ' + dados['animal'])
        print('Data da adocao: ' + dados['data'].strftime('%d/%m/%Y'))
        print('Numero do chip: ' + str(dados['chip']))
        print('CPF do adotante: ' + dados['cpf'])
        print('Assinou o termo de responsabilidade: ' + "SIM" if dados['assinou_termo'] else "NAO")
