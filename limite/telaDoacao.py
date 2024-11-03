from limite.telaAbstrata import TelaAbstrata
from datetime import datetime
from verificacao import verificaCPF
from exception.CPFexception import CPFExecption


class TelaDoacao(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Doacao ----------")
        print("Escolha a opcao")
        print("0 - Retornar")
        print("1 - Registrar Doacao")
        print("2 - Listar Doacoes")

        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2])
        return opcao

    def pega_dados_doacao(self):
        print("-------- Dados Doacao (Digite 0 para retornar) ----------")
        cpf = input("CPF: ").replace(".", "").replace("-", "").strip()
        while True:
            if cpf == '0':
                return 0
            try:
                verificaCPF(cpf)
                break
            except (CPFExecption, ValueError):
                print("O CPF digitado está incorreto, por favor o digite novamente.")
                cpf = input("CPF: ")

        data = input("Data (formato DD/MM/YYYY): ")
        while True:
            if data == '0':
                return 0
            try:
                data = datetime.strptime(data, '%d/%m/%Y')
                break
            except: 
                print('Data invalida inserida.')
                data = input("Data (formato DD/MM/AAAA): ")

        animal = {}
        # Pensando em fazer um try/except para cada input e tirar o geral
        tipo_animal = input('Tipo de animal (Gato/Cachorro): ')
        while True:
            if tipo_animal == '0':
                return 0
            try:
                tipo_animal.lower()
                if tipo_animal == 'cachorro':
                    tamanho_animal = input('Tamanho do animal (P/M/G): ')
                    while True:
                        if tipo_animal == '0':
                            return 0
                        try:
                            if tamanho_animal not in ['P', 'p', 'M', 'm', 'G', 'g']:
                                raise ValueError
                            else:
                                break
                        except:
                            print('Tamanho invalido inserido.')
                            tamanho_animal = input('Tamanho do animal (P/M/G): ')
                    animal.update({'tamanho': tamanho_animal})
                    break
                elif tipo_animal == 'gato':
                    break
                else:
                    raise ValueError
            except:
                print('Tipo de animal invalido.')
                tipo_animal = input('Tipo de animal (Gato/Cachorro): ')
        animal.update({'tipo': tipo_animal})

        chip_animal = input('Numero do chip do animal: ')
        while True:
            if chip_animal == '0':
                return 0
            try:
                chip_animal = int(chip_animal)
                if chip_animal < 0:
                    raise ValueError
                break
            except:
                print('Valor de chip invalido.')
                chip_animal = input('Numero do chip do animal: ')
        animal.update({'chip': chip_animal})

        nome_animal = input('Nome do animal: ')
        if nome_animal == '0':
            return 0
        #Adicionar checagem para nome so terem letras ?
        animal.update({'nome': nome_animal})

        raca_animal = input('Raca do animal: ')
        if raca_animal == '0':
            return 0
        #Verificar para ver se raca so tem letras 
        animal.update({'raca': raca_animal})

        print('Cadastro de Vacinas')
        vacinas_animal = []

        while True:
            print("0- Retornar")
            print("1- Cadastrar nova vacina")
            opcao = input()
            while opcao not in ["1", "0"]:
                opcao = input("Por favor, escolha uma opcao valida: ")
            if opcao == '2':
                break
            else:
                print("Qual dessas vacinas voce quer cadastrar?")
                print("0- Retornar")
                print("1- Raiva")
                print("2- Hepatite")
                print("3- Leptospirose")
                opcao2 = input()
                while opcao2 not in ['1', '2', '3', '0']:
                    print("Por favor, digite uma opcao valida: ")
                    opcao2 = input()
                if opcao2 == 4:
                    break
                else:
                    data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
                    while True:
                        try:
                            data_vacina = datetime.strptime(data_vacina, '%d/%m/%Y')
                        except:
                            print("Por favor, digite uma data valida")
                            data_vacina = input("Data de aplicacao da vacina (DD/MM/YYYY): ")
                    
            vacinas_animal.append({'data': data_vacina, 'nome': int(opcao2), 'animal': chip_animal})
        animal.update({'vacinas': vacinas_animal})

        motivo = input("Qual o motivo da doacao? ")
        if motivo == '0':
            return 0

        return {"data": data, "animal": animal, "cpf": cpf, "motivo": motivo}

    def mostrar_doacao(self, dados):
        print('--------' + ' Animal: ' + dados['animal'] + ' ----------')
        print('Data da doacao: ' + dados['data'].strftime('%d/%m/%Y'))
        print('Numero do chip: ' + str(dados['chip']))
        print('CPF do doador: ' + dados['cpf'])
        print('Motivo da doacao: ' + dados['motivo'])
        
    def mensagem_sem_doador(self):
        print("Doador nao encontrado no sistema")

    def mensagem_sem_doacoes(self):
        print("Nao existem doacoes cadastradas no sistema")