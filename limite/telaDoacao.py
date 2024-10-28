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
        print("-------- Dados Doacao ----------")
        #Adicionar verificacao de tipo para cada um desses dados
        try:
            cpf = input("CPF: ").replace(".", "").replace("-", "").strip()
            while True:
                try:
                    verificaCPF(cpf)
                    break
                except (CPFExecption, ValueError):
                    print("O CPF digitado está incorreto, por favor o digite novamente.")
                    cpf = input("CPF: ")

            data = input("Data (formato dia/mes/ano): ")
            while True:
                try:
                    data = datetime.strptime(data, '%d/%m/%Y')
                    break
                except: 
                    print('Data invalida inserida.')
                    data = input("Data (formato dia/mes/ano): ")

            animal = {}
            # Pensando em fazer um try/except para cada input e tirar o geral
            tipo_animal = input('Tipo de animal (Gato/Cachorro): ')
            if tipo_animal == 'Cachorro':
                tamanho_animal = input('Tamanho do animal (P/M/G): ')
                if tamanho_animal not in ['P', 'M', 'G']:
                    raise ValueError
                animal.update({'tamanho': tamanho_animal})
            elif tipo_animal == 'Gato':
                pass
            else:
                raise ValueError
            animal.update({'tipo': tipo_animal})

            chip_animal = input('Numero do chip do animal: ')
            chip_animal = int(chip_animal)
            animal.update({'chip': chip_animal})

            nome_animal = input('Nome do animal: ')
            animal.update({'nome': nome_animal})

            raca_animal = input('Raca do animal: ')
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

            return {"data": data, "animal": animal, "cpf": cpf, "motivo": motivo}
        except ValueError:
            print('Valor inserido invalido')

    def mostrar_doacao(self, dados):
        print('--------' + ' Animal: ' + dados['animal'] + ' ----------')
        print('Data da doacao: ' + dados['data'].strftime('%d/%m/%Y'))
        print('Numero do chip: ' + str(dados['chip']))
        print('CPF do doador: ' + dados['cpf'])
        print('Motivo da doacao: ' + dados['motivo'])
        