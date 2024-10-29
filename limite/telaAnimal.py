from limite.telaAbstrata import TelaAbstrata


class TelaAnimal(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- ONG de Animais ---------")
        print("Escolha sua opcao")
        print("0 - Retornar")
        print("1 - Cachorros")
        print('2 - Gatos')
        
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2])
        return opcao