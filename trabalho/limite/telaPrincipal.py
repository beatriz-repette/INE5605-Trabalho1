from limite.telaAbstrata import TelaAbstrata


class TelaPrincipal(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- ONG de Animais ---------")
        print("Escolha sua opcao")
        print("0 - Finalizar sistema")
        print("1 - Registrar Doador")
        print("2 - Registrar Doação")
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2])
        return opcao
