from limite.telaAbstrata import TelaAbstrata
from datetime import date, datetime
from verificacao import verificaCPF
from exception.CPFexception import CPFExecption


class TelaAdocao(TelaAbstrata):
    def tela_opcoes(self): #Anteriormente funcao chamava-se "mostrar_opcoes"
        print("-------- Adocao ----------")
        print("Escolha a opcao")
        print("0 - Retornar")
        print("1 - Registrar Adocao")
        print('2 - Alterar Adocao')
        print("3 - Listar Adocoes")
        print('4 - Excluir Adocao')
        print('5 - Relatorio de Adocoes')

        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2, 3, 4, 5])
        return opcao

    def pega_dados_adocao(self):
        print("-------- Dados Adocao (Digite 0  para retornar) ----------")
        #Adicionar verificacao de tipo para cada um desses dados
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

        animal = input('Chip do animal: ')
        while True:
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
    
    def pega_dados_alterados_adocao(self):
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
    
    def seleciona_adocao(self, len):
        adocao = input("Posicao da adocao na database (Digite * para retornar): ")
        while True:
            if adocao == '*':
                break
            try:
                adocao = int(adocao)
                if adocao < 0 or adocao >= len:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, insira uma posicao valida.")
                adocao = input("Posicao da adocao na database (Digite * para retornar): ")
        return adocao
    
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
        print('-------- Adocao:', n, '----------')
        print('Animal: ' + dados['animal'])
        print('Data da adocao: ' + dados['data'].strftime('%d/%m/%Y'))
        print('Numero do chip: ' + str(dados['chip']))
        print('CPF do adotante: ' + dados['cpf'])
        print('Assinou o termo de responsabilidade: ' + "SIM" if dados['assinou_termo'] else "NAO")

    def mensagem_sem_adotante(self):
        print("Sem adotantes no sistema")

    def mensagem_sem_adocoes(self):
        print("Nao existem adocoes no sistema")

    def mensagem_menor_idade(self):
        print("Para realizar uma adocao, o adotante precisa ter mais de 18 anos.")

    def mensagem_ja_doou(self):
        print("Para realizar uma adocao, o adotante nao pode ja ter doado um animal.")

    def mensagem_no_animal(self):
        print("Esse animal nao foi encontrado no sistema.")

    def mensagem_vacs_invalidas(self):
        print("Esse animal nao possui todas as vacinas necessarias para poder ser adotado.")

    def mensagem_residencia_incompativel(self):
        print("Tamanho do animal incompativel com a sua residencia.")

    def mensagem_ja_adotado(self):
        print("O animal ja foi adotado.")