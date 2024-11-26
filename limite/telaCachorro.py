from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
from verificacao import verificaNome
from exception.erroCadastroException import ErroCadastroException
import PySimpleGUI as sg


class TelaCachorro(TelaAbstrata):
    def tela_opcoes(self):
        layout = [
        [sg.Radio('Ver cachorros', "RADIO1", key = 1, default = True, size=(10
        ,1))],
        [sg.Radio('Adicionar vacina', "RADIO1", key = 2)],
        [sg.Radio('Alterar cachorros', "RADIO1", key = 3)],
        [sg.Radio('Excluir cachorros', "RADIO1", key = 4)],
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
    
    def seleciona_cachorro(self):
        chip = input("Chip do cachorro (Digite * para retornar): ")
        while True:
            if chip == '*':
                break
            try:
                chip = int(chip)
                if chip < 0:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, insira um chip valido.")
                chip = input("Chip do cachorro (Digite * para retornar): ")
        return chip

    def mostrar_cachorro(self, dados):
        print('--------' + ' Cachorro: ' + dados['animal'] + ' ----------')
        print('Numero do chip: ' + str(dados['chip']))
        print('Tamanho: ' + dados['tamanho'])
        print('Raca: ' + dados['raca'])
        print('Vacinas:', dados['vacinas'])
        print('Foi adotado:', 'Sim' if dados['adotado'] else 'Nao')
        
    def mensagem_sem_cachorros(self):
        print("Nao existem cachorros cadastrados no sistema")

    def mensagem_erro_vacina(self):
        print('Erro ao adicionar vacinas.')

    def pegar_dados_cachorro(self):
        print("-------- Alteracao de cachorro (insira 0 para retornar ou * para avançar) ---------")
        cachorro = {}

        # Verificacao de nome
        nome = input("Nome do cachorro: ")
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
        cachorro.update({'nome': nome})

        while True:
            try:
                chip = input('Chip do cachorro: ')
                if chip == '*':
                    break
                chip = int(chip)
                if chip < 0:
                    raise ValueError
                break

            except ValueError:
                print('Por favor, insira um chip invalido.')
                chip = input('Chip do cachorro: ')
        cachorro.update({'chip': chip})

        raca = input('Raca do cachorro: ')
        if raca == '0':
            return 0
        cachorro.update({'raca': raca})

        while True:
            tamanho = input('Tamanho do cachorro: ')
            if tamanho == '0':
                return 0
            elif tamanho == '*':
                break
            try:
                tamanho = tamanho.upper()
                if tamanho not in ['P', 'M', 'G']:
                    raise ValueError
                break
            except:
                print('Por favor, insira um tamanho valido.')
                tamanho = input('Tamanho do cachorro: ')
        cachorro.update({'tamanho': tamanho})

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
        cachorro.update({'vacinas': vacinas_animal})
        return cachorro

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
    
    def mostrar_mensagem(self, mensagem):
        print(mensagem)