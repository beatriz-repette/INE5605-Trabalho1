from verificacao import verificaCPF
from exception.CPFexception import CPFExecption


class TelaAdotante():
    def tela_opcoes(self): # Anteriormente funcao chamava-se "mostrar_opcoes"
        print("-------- Doador ----------")
        print("Escolha a opcao")
        print("1 - Incluir Adotante")
        print("2 - Alterar Adotante")
        print("3 - Listar Adotantes")
        print("4 - Excluir Adotante")
        print("0 - Retornar")

        opcao = input("Escolha a opcao: ")
        while opcao not in ["1" ,"2" ,"3" ,"4" ,"0"]:
            print("Input invalido, por favor digite uma das opcoes validas")
            opcao = input("Escolha a opcao: ")

        return int(opcao)

    def pega_dados_adotante(self):
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
        data_nascimento = input("Data de nascimento:") # Verificacao para variavel do tipo Date
        endereco = input("Endereco: ")
        tipo_habitacao = input("Tipo de habitação: ") #Relacionar isso à classe "Tipo Habitacao"
        possui_animal = input("Possui animal? (sim/nao) ") #Converter para bool

        return {"nome": nome, "endereco": endereco, "data_nascimento" :data_nascimento, "cpf": cpf, "tipo_habitacao" : tipo_habitacao, "possui_animal" : possui_animal}

    def seleciona_adotante(self):
        # Adicionar verificacao de tipo para o cpf
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_adotante(self, dados_adotante):
        print("NOME DO AMIGO: ", dados_adotante["nome"])
        print("CPF DO AMIGO: ", dados_adotante["cpf"])
        print("DATA NASCIMENTO: ", dados_adotante["data_nascimento"])
        print("ENDERECO: ", dados_adotante["endereco"])
        print("TIPO DE HABITAÇÃO: ", dados_adotante["tipo_habitacao"])
        print("POSSUI ANIMAL? ", "SIM" if dados_adotante["possui_animal"] == True else "NÃO")
        print("\n")
