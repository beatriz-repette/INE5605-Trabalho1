from verificacao import verificaCPF
from limite.telaAbstrata import TelaAbstrata
from exception.CPFexception import CPFExecption
from datetime import date, datetime


class TelaDoador(TelaAbstrata):
    def tela_opcoes(self): #Anteriormente funcao chamava-se "mostrar_opcoes"
        print("-------- Doador ----------")
        print("Escolha a opcao")
        print("0 - Retornar")
        print("1 - Incluir Doador")
        print("2 - Alterar Doador")
        print("3 - Listar Doadores")
        print("4 - Excluir Doador")

        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_doador(self):
        print("-------- Dados Doador ----------")

        #Verificacao CPF
        cpf = input("CPF: ").replace(".", "").replace("-", "").replace(" ", "")
        while True:
            try:
                verificaCPF(cpf)
                break
            except CPFExecption or ValueError:
                print("O CPF digitado está incorreto, por favor o digite novamente.")
                cpf = input("CPF: ")

        nome = input("Nome: ")
        data = input("Data de nascimento (formato dia/mes/ano): ")
        while True:
            try:
                data = datetime.strptime(data, '%d/%m/%Y')
                break
            except: 
                print('Data invalida inserida.')
                data = input("Data de nascimento (formato dia/mes/ano): ")

        endereco = input("Endereco: ")


        return {"nome": nome, "endereco": endereco, "data_nascimento": data, "cpf": cpf}
    
    def seleciona_doador(self):
        #Adicionar verificacao de tipo para o cpf
        cpf = input("CPF do doador que deseja selecionar: ")
        return cpf

    def mostra_doador(self, dados_doador):
        print('------------------')
        print("NOME DO DOADOR:", dados_doador["nome"])
        print("CPF DO DOADOR:", dados_doador["cpf"])
        print("DATA NASCIMENTO:", dados_doador["data_nascimento"].strftime('%d/%m/%Y'))
        print("ENDERECO:", dados_doador["endereco"])
