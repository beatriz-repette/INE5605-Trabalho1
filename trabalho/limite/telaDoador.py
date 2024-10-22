from limite import telaAbstrata
from limite.telaAbstrata import TelaAbstrata


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
        #Adicionar verificacao de tipo para cada um desses dados
        cpf = input("CPF: ")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento:") #Verificacao para variavel do tipo Date
        endereco = input("Endereco: ")


        return {"nome": nome, "endereco": endereco, "data_nascimento":data_nascimento, "cpf": cpf}
    
    def seleciona_doador(self):
        #Adicionar verificacao de tipo para o cpf
        cpf = input("CPF do doador que deseja selecionar: ")
        return cpf
