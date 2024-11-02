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
        print("2 - Listar Adocoes")

        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2])
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
            try:
                assinou_termo = assinou_termo.lower()
                if assinou_termo == '0':
                    return 0
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

    def mostrar_adocao(self, dados):
        print('--------' + ' Animal: ' + dados['animal'] + ' ----------')
        print('Data da adocao: ' + dados['data'].strftime('%d/%m/%Y'))
        print('Numero do chip: ' + str(dados['chip']))
        print('CPF do adotante: ' + dados['cpf'])
        print('Assinou o termo de responsabilidade: ' + "SIM" if dados['assinou_termo'] else "NAO")