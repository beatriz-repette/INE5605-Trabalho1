import verificacao
from verificador.verificaCPF import verificaCPF
from exception.CPFexception import CPFExecption


class TelaDoador():
    def tela_opcoes(self): #Anteriormente funcao chamava-se "mostrar_opcoes"
        print("-------- Doador ----------")
        print("Escolha a opcao")
        print("1 - Incluir Doador")
        print("2 - Alterar Doador")
        print("3 - Listar Doadores")
        print("4 - Excluir Doador")
        print("0 - Retornar")

        opcao = input("Escolha a opcao: ")
        while opcao not in ["1","2","3","4","0"]:
            print("Input invalido, por favor digite uma das opcoes validas")
            opcao = input("Escolha a opcao: ")
        
        return int(opcao)

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
        data_nascimento = input("Data de nascimento:") #Verificacao para variavel do tipo Date
        endereco = input("Endereco: ")


        return {"nome": nome, "endereco": endereco, "data_nascimento":data_nascimento, "cpf": cpf}
    
    def seleciona_doador(self):
        #Adicionar verificacao de tipo para o cpf
        cpf = input("CPF do doador que deseja selecionar: ")
        return cpf

    def mostra_doador(self, dados_doador):
        print("NOME DO AMIGO: ", dados_doador["nome"])
        print("CPF DO AMIGO: ", dados_doador["cpf"])
        print("DATA NASCIMENTO: ", dados_doador["data_nascimento"])
        print("ENDERECO: ", dados_doador["endereco"])
        print("\n")
