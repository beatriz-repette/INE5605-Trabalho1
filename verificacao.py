from exception.CPFexception import CPFExecption
from exception.nomeException import NomeException
from exception.enderecoException import EnderecoException
from exception.erroCadastroException import ErroCadastroException
#Classe para armazenar funcoes de verificacao

#Lembrete: o CPF é armazenado no sistema como string sem "." nem "-"
def verificaCPF(cpf):
        cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")

        try:
            listacpf = [int(x) for x in list(cpf)]
        except ValueError:
            raise CPFExecption

        #Verifica num de digitos
        if len(listacpf) != 11:
            raise CPFExecption

        #Verifica CPF de unico digito repetido
        if len(set(listacpf)) == 1:
            raise CPFExecption

        #Digito verificador 1
        ver1 = sum((10 - i) * listacpf[i] for i in range(9)) % 11

        if ver1 < 2:
            ver1 = 0
        else:
            ver1 = 11 - ver1
            
        if ver1 != listacpf[9]:
            raise CPFExecption

        #Digito verificador 2
        ver2 = sum((11 - i) * listacpf[i] for i in range(10)) % 11

        if ver2 < 2:
            ver2 = 0
        else:
            ver2 = 11 - ver2

        if ver2 != listacpf[10]:
            raise CPFExecption

# Para se ter um endereco valido eh preciso que a entrada tenha pelo menos uma letra,
# um numero e um espaco (para simular uma entrada de endereco com nome de rua, numero, etc...

def verificaEndereco(e):
    if (any(c.isalpha() for c in e) and any(c.isspace() for c in e)) and any(c.isdigit() for c in e):
        pass
    else:
        raise EnderecoException

def verificaNome(nome):
    nome = nome.replace(" ","")
    if nome.isalpha():
        pass
    else:
        raise NomeException

def verificaChip(chip):
    if chip.isdigit(): #Verificar se o "-" conta como digito
        pass
    else:
        raise ChipException
