from funcaoB import *

def OpreacaoDeCadastro(Dic):
    cpf = Dic[1]
    senha = Dic[4]
    confirmasenha = Dic[5]
    if checar('Clientes', cpf):
        print('CPF já cadastrado!')           
    else:
        if senha == confirmasenha:
            Dados = (Dic[0], Dic[1], Dic[2], Dic[3], Dic[4], 0)
            GravarNoBancoClientes(Dados)
            return True
        else:
            print('Ambas as senhas devem ser iguais!')

