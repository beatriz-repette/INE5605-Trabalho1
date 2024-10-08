from telas.telaAbstrata import TelaAbstrata


class TelaDoacao(TelaAbstrata):
    def __init__(self, controlador) -> None:
        self.__controlador = controlador

    def tela_opcoes(self): #Anteriormente funcao chamava-se "mostrar_opcoes"
        print("-------- Doacao ----------")
        print("Escolha a opcao")
        print("0 - Retornar")
        print("1 - Registrar Doacao")
        print("2 - Listar Doacoes")
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2])
        return opcao

    def pega_dados_doacao(self):
        print("-------- Dados Doacao ----------")
        #Adicionar verificacao de tipo para cada um desses dados
        data = input("Data: ")
        animal = input("Animal: ")
        cpf = input("CPF: ")
        motivo = input("Motivo: ")


        return {"data": data, "animal": animal, "cpf": cpf, "motivo": motivo}
    