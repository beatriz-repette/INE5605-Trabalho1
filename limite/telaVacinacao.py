from limite.telaAbstrata import TelaAbstrata
from datetime import datetime

class TelaVacinacao(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Historico de Vacinacao ---------")
        print("Escolha sua opcao")
        print("0 - Retornar")
        print("1 - Ver vacinacoes")
        print('2 - Adicionar vacinacao')
        print('3 - Excluir vacinacao')
        
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2, 3])
        return opcao
    
    def pegar_vacina(self):
        print('-------------- Cadastro de Vacinacao ---------------')
        vacinas_animal = []

        while True:
            chip_animal = input("Chip do animal: ")
            try:
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
    
    def mostrar_vacinacao(self, dados):
        print('------------------')
        print('Data da vacina:', dados['data'].strftime('%d/%m/%Y'))
        print('Nome da vacina:', dados['nome'])
        print('Nome do animal:', dados['animal'])

    def selecionar_vacinacao(self):
        chip = input('Chip do animal que recebeu a vacina: ')
        while True:
            try:
                chip = int(chip)
                if chip < 0:
                    raise ValueError
                break
            except:
                print('Por favor, insira um chip valido.')
                chip = input('Chip do animal que recebeu a vacina: ')

        vacina = input('Nome da vacina que foi recebida: ')
        while True:
            try:
                vacina = vacina.upper()
                if vacina not in ['RAIVA', 'HEPATITE', 'LEPTOSPIROSE']:
                        raise ValueError
                break
            except:
                print('Por favor, insira uma vacina valida.')
                vacina = input('Nome da vacina que foi recebida: ')

        data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
        while True:
            try:
                data_vacina = datetime.strptime(data_vacina, '%d/%m/%Y')
                break
            except:
                print("Por favor, digite uma data valida")
                data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
        return {'chip': chip, 'vacina': vacina, 'data': data_vacina}

    
    def mostrar_mensagem(self, mensagem):
        if isinstance(mensagem, str):
            print(mensagem)