from limite.telaAbstrata import TelaAbstrata


class TelaCachorro(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- ONG de Animais ---------")
        print("Escolha sua opcao")
        print("0 - Retornar")
        print("1 - Ver Cachorros")
        
        opcao = self.ler_int('Escolha uma opcao: ', [0, 1])
        return opcao

    def mostrar_cachorro(self, dados):
        print('--------' + ' Cachorro: ' + dados['animal'] + ' ----------')
        print('Numero do chip: ' + str(dados['chip']))
        print('Tamanho: ' + dados['tamanho'])
        print('Raca: ' + dados['raca'])
        print('Foi adotado:', 'Sim' if dados['adotado'] else 'Nao')

    def mensagem_sem_cachorros(self):
        print("Nao existem cachorros cadastrados no sistema")
