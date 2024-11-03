from verificacao import verificaCPF
from limite.telaAbstrata import TelaAbstrata
from exception.CPFexception import CPFExecption
from datetime import datetime


class TelaDoador(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Doador ----------")
        print("Escolha uma opcao:")
        print("0 - Retornar")
        print("1 - Incluir Doador")
        print("2 - Alterar Doador")
        print("3 - Listar Doadores")
        print("4 - Excluir Doador")

        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_doador(self):
        print("-------- Dados Doador (Digite 0 para retornar) ----------")

        #Verificacao CPF
        cpf = input("CPF: ").replace(".", "").replace("-", "").replace(" ", "")
        while True:
            if cpf == '0':
                return 0
            try:
                verificaCPF(cpf)
                break
            except CPFExecption or ValueError:
                print("O CPF digitado está incorreto, por favor o digite novamente.")
                cpf = input("CPF: ").replace(".", "").replace("-", "").replace(" ", "")

        nome = input("Nome: ")
        if nome == '0':
            return 0

        data = input("Data de nascimento (formato DD/MM/YYYY): ")
        while True:
            if data == '0':
                return 0
            try:
                data = datetime.strptime(data, '%d/%m/%Y')
                break
            except: 
                print('Data invalida inserida.')
                data = input("Data de nascimento (formato dia/mes/ano): ")

        endereco = input("Endereco: ")
        if nome == '0':
            return 0

        return {"nome": nome, "endereco": endereco, "data_nascimento": data, "cpf": cpf}
    
    def seleciona_doador(self):
        cpf = input("CPF do doador que deseja selecionar: ").replace(".", "").replace("-", "").replace(" ", "")
        while True:
            if cpf == '0':
                return 0
            try:
                verificaCPF(cpf)
                break
            except CPFExecption or ValueError:
                print("O CPF digitado está incorreto, por favor o digite novamente.")
                cpf = input("CPF: ").replace(".", "").replace("-", "").replace(" ", "")


    def mostra_doador(self, dados_doador):
        print('------------------')
        print("NOME DO DOADOR:", dados_doador["nome"])
        print("CPF DO DOADOR:", dados_doador["cpf"])
        print("DATA NASCIMENTO:", dados_doador["data_nascimento"].strftime('%d/%m/%Y'))
        print("ENDERECO:", dados_doador["endereco"])

    def mensagem_erro_cadastro(self):
        print("Erro ao cadastrar doador, CPF inserido ja cadastrado")

    def mensagem_doador_nao_existente(self):
        print("Nao existe nenhum cadastro de doador com esse CPF")

    def mensagem_non_existent(self):
        print("Nao existem doadores no sistema")
