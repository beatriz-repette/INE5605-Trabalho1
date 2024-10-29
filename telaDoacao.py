from limite.telaAbstrata import TelaAbstrata
from datetime import date, datetime
from verificacao import verificaCPF
from exception.CPFexception import CPFExecption


class TelaDoacao(TelaAbstrata):
    def tela_opcoes(self): #Anteriormente funcao chamava-se "mostrar_opcoes"
        print("-------- Doacao ----------")
        print("Escolha a opcao")
        print("0 - Retornar")
        print("1 - Registrar Doacao")
        print("2 - Listar Doacoes")

        opcao = self.ler_int('Escolha uma opcao: ', [0, 1, 2])
        return opcao

    def pega_dados_doacao(self):
        print("-------- Dados Doacao (Digite 0 para retornar) ----------")
        #Adicionar verificacao de tipo para cada um desses dados
        cpf = input("CPF: ").replace(".", "").replace("-", "").strip()
        while True:
            if cpf == '0':
                return 0
            try:
                verificaCPF(cpf)
                break
            except (CPFExecption, ValueError):
                print("O CPF digitado está incorreto, por favor o digite novamente.")
                cpf = input("CPF: ")

        data = input("Data (formato dia/mes/ano): ")
        while True:
            if data == '0':
                return 0
            try:
                data = datetime.strptime(data, '%d/%m/%Y')
                break
            except: 
                print('Data invalida inserida.')
                data = input("Data (formato dia/mes/ano): ")

        animal = {}
        # Pensando em fazer um try/except para cada input e tirar o geral
        tipo_animal = input('Tipo de animal (Gato/Cachorro): ')
        while True:
            if tipo_animal == '0':
                return 0
            try:
                if tipo_animal == 'Cachorro':
                    tamanho_animal = input('Tamanho do animal (P/M/G): ')
                    while True:
                        if tipo_animal == '0':
                            return 0
                        try:
                            if tamanho_animal not in ['P', 'p', 'M', 'm', 'G', 'g']:
                                raise ValueError
                            else:
                                break
                        except:
                            print('Tamanho invalido inserido.')
                            tamanho_animal = input('Tamanho do animal (P/M/G): ')
                    animal.update({'tamanho': tamanho_animal})
                    break
                elif tipo_animal == 'Gato':
                    break
                else:
                    raise ValueError
            except:
                print('Tipo de animal invalido.')
                tipo_animal = input('Tipo de animal (Gato/Cachorro): ')
        animal.update({'tipo': tipo_animal})

        chip_animal = input('Numero do chip do animal: ')
        while True:
            try:
                chip_animal = int(chip_animal)
                break
            except:
                print('Valor de chip invalido.')
                chip_animal = input('Numero do chip do animal: ')
        animal.update({'chip': chip_animal})

        nome_animal = input('Nome do animal: ')
        if nome_animal == '0':
            return 0
        animal.update({'nome': nome_animal})

        raca_animal = input('Raca do animal: ')
        if raca_animal == '0':
            return 0
        animal.update({'raca': raca_animal})

        print('Vacinas do animal (Digite 0 para encerrar):')
        vacinas_animal = []
        while True:
            data_vacina = input("Data da vacina(formato dia/mes/ano): ")
            if data_vacina == '0':
                break
            data_vacina = datetime.strptime(data_vacina, '%d/%m/%Y')
            nome_vacina = input('Vacina: ')
            if nome_vacina == '0':
                break
            vacinas_animal.append({'data': data_vacina, 'nome': nome_vacina, 'animal': chip_animal})
        animal.update({'vacinas': vacinas_animal})

        motivo = input("Motivo: ")
        if motivo == '0':
            return 0

        return {"data": data, "animal": animal, "cpf": cpf, "motivo": motivo}

    def mostrar_doacao(self, dados):
        print('--------' + ' Animal: ' + dados['animal'] + ' ----------')
        print('Data da doacao: ' + dados['data'].strftime('%d/%m/%Y'))
        print('Numero do chip: ' + str(dados['chip']))
        print('CPF do doador: ' + dados['cpf'])
        print('Motivo da doacao: ' + dados['motivo'])
        