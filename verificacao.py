from exception.CPFexception import CPFExecption
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
        ver1 = (10 * listacpf[0] + 9 * listacpf[1] + 8 * listacpf[2] + 7 * listacpf[3]
                + 6 * listacpf[4] + 5 * listacpf[5] + 4 * listacpf[6] + 3 * listacpf[7] + 2 * listacpf[8]) % 11
        if ver1 >= 10:
            ver1 = 0
        if ver1 != (11 - listacpf[9]):
            raise CPFExecption
