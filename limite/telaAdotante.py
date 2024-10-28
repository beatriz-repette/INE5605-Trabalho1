from verificacao import verificaCPF
from exception.CPFexception import CPFExecption
from limite.telaAbstrata import TelaAbstrata
from datetime import datetime, date


class TelaAdotante(TelaAbstrata):
    def tela_opcoes(self): # Anteriormente funcao chamava-se "mostrar_opcoes"
        print("-------- Adotante ----------")
        print("Escolha a opcao:")
        print("0 - Retornar")
        print("1 - Incluir Adotante")
        print("2 - Alterar Adotante")
        print("3 - Listar Adotantes")
        print("4 - Excluir Adotante")

        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_adotante(self):
        print("-------- Dados Adotante ----------")
        #Verificacao CPF
        cpf = input("CPF: ").replace(".", "").replace("-", "").strip()
        while True:
            try:
                verificaCPF(cpf)
                break
            except (CPFExecption, ValueError):
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

        print('Tipos de habitacao: Casa (1), Apartamento Pequeno (2), Medio (3) ou Grande (4)')
        tipo_habitacao = input("Tipo de habitação: ") #Relacionar isso à classe "Tipo Habitacao"
        while True:
            try:
                tipo_habitacao = int(tipo_habitacao)
                if tipo_habitacao in [1, 2, 3, 4]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Valor invalido inserido.')
                tipo_habitacao = input("Tipo de habitação: ")

        possui_animal = input("Possui animal? (sim/nao): ") #Converter para bool
        while True:
            if possui_animal in ['sim', 'Sim']:
                possui_animal = True
                break
            elif possui_animal in ['nao', 'Nao']:
                possui_animal = False
                break
            else:
                print('Insira uma opcao valida')
                possui_animal = input("Possui animal? (sim/nao): ")

        return {"nome": nome, "endereco": endereco, "data_nascimento": data, "cpf": cpf, "tipo_habitacao": tipo_habitacao, "possui_animal": possui_animal}

    def seleciona_adotante(self):
        # Adicionar verificacao de tipo para o cpf
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_adotante(self, dados_adotante):
        print("------------------")
        print("NOME DO ADOTANTE:", dados_adotante["nome"])
        print("CPF DO ADOTANTE:", dados_adotante["cpf"])
        print("DATA NASCIMENTO:", dados_adotante["data_nascimento"].strftime('%d/%m/%Y'))
        print("ENDERECO:", dados_adotante["endereco"])
        print("TIPO DE HABITACAO:", dados_adotante["tipo_habitacao"])
        print("POSSUI ANIMAL?:", "SIM" if dados_adotante["possui_animal"] == True else "NAO")
