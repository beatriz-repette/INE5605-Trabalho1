

class TelaPrincipal():
    def tela_opcoes(self):
        print("-------- ONG de Animais ---------")
        print("Escolha sua opcao")
        print("1 - Doador")
        print("0 - Finalizar sistema")

        opcao = input("Escolha a opcao: ")
        while opcao not in ["1","0"]: #Adicionar opcoes a medida que novas telas forem sendo adicionadas
            print("Input invalido, por favor digite uma das opcoes validas")
            opcao = input("Escolha a opcao: ")

        return int(opcao)
