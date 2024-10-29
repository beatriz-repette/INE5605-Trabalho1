from limite.telaAbstrata import TelaAbstrata


class TelaPrincipal(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- ONG de Animais ---------")
        print("Escolha sua opcao")
        print("0 - Finalizar sistema")
        print("1 - Doador")
        print('2 - Adotante')
        print("3 - Doacao")
        print('4 - Adocao')
        print('5 - Animais')
        
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2, 3, 4, 5])
        return opcao