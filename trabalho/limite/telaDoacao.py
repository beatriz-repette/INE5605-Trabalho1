from entidade.cachorro import Cachorro
from limite.telaAbstrata import TelaAbstrata
from datetime import date, datetime


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
            data = input("Data (formato dia/mes/ano): ")
            data = datetime.strptime(data, '%d/%m%/Y')

            animal = {}
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
            animal.update({'chip': chip_animal})
            nome_animal = input('Nome do animal: ')
            animal.update({'nome': nome_animal})
            raca_animal = input('Raca do animal: ')
            animal.update({'raca': raca_animal})
            vacinas_animal = []
            print('Vacinas do animal: ', end = '')
            data_vacina = 1
            while data_vacina != 0:
                data_vacina = input("Data da vacina(formato dia/mes/ano): ")
                data_vacina = datetime.strptime(data_vacina, '%d/%m%/Y')
                nome_vacina = input('Vacina: ')
                vacinas_animal.append({'data': data_vacina, 'nome': nome_vacina})
            animal.update({'vacinas': vacinas_animal})

            cpf = input("CPF do doador: ")
            if len(cpf) != 11:
                raise ValueError
            
            motivo = input("Motivo: ")

            return {"data": data, "animal": animal, "cpf": cpf, "motivo": motivo}
        except ValueError:
            print('Valor inserido inválido')

    def mostrar_doacao(self, dados):
        print('--------' + ' Animal: ' + dados['animal'] + ' ----------')
        print('Data da doacao: ' + dados['data'])
        print('CPF do doador: ' + dados['cpf'])
        print('Motivo da doacao: ' + dados['motivo'])
        