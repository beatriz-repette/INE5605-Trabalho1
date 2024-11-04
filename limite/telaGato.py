from limite.telaAbstrata import TelaAbstrata
from datetime import datetime

class TelaGato(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- ONG de Animais ---------")
        print("Escolha sua opcao")
        print("0 - Retornar")
        print("1 - Ver gatos")
        print('2 - Adicionar vacina')
        print('3 - Alterar gato')
        print('4 - Excluir gato')
        
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2, 3, 4])
        return opcao
    
    def pegar_dados_gato(self):
        print("-------- Alteracao de gato (insira 0 para retornar ou * para avançar) ---------")
        gato = {}

        nome = input('Nome do gato: ')
        if nome == '0':
            return 0
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
                print('Por favor, insira um chip invalido.')
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
        print('--------' + ' Gato: ' + dados['animal'] + ' ----------')
        print('Numero do chip: ' + str(dados['chip']))
        print('Raca: ' + dados['raca'])
        print('Vacinas:', dados['vacinas'])
        print('Foi adotado:', 'Sim' if dados['adotado'] else 'Nao')

    def seleciona_gato(self):
        chip = input("Chip do gato (Digite * para retornar): ")
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
                chip = input("Chip do gato (Digite * para retornar): ")
        return chip

    def mensagem_sem_gatos(self):
        print("Nao existem gatos cadastrados no sistema")

    def mensagem_erro_vacina(self):
        print('Erro ao adicionar vacinas.')

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
