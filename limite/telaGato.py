from limite.telaAbstrata import TelaAbstrata


class TelaGato(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- ONG de Animais ---------")
        print("Escolha sua opcao")
        print("0 - Retornar")
        print("1 - Ver Gatos")
        
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1])
        return opcao

    def mostrar_cachorro(self, dados):
        print('--------' + ' Gato: ' + dados['animal'] + ' ----------')
        print('Numero do chip: ' + str(dados['chip']))
        print('Raca: ' + dados['raca'])
        print('Foi adotado:', 'Sim' if dados['adotado'] else 'Nao')

    def mensagem_sem_gatos(self):
        print("Nao existem gatos cadastrados no sistema")