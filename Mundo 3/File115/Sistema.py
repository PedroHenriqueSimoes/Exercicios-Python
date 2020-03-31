from File115.lib.Interfarce import *
from File115.lib.Arquivo import *
from uteis.numeros import LeiaInt
from time import sleep

arq = 'pessoas.txt'

if arqExiste(arq):
    print('Arquivo encontrado com sucesso !')
else:
    print('Arquivo não encontrado')
    criararq(arq)
while True:
    resp = menu(['Ver lista', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resp == 1:
        #Lista conteudo
        LerArquivo(arq)
    elif resp == 2:
        cab('Novo Cadastro')
        nome = (str(input('Nome: ')))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cab('Saindo do programa... Volte sempre !')
        break
    else:
        print('\033[31mDigite uma opção valida !\033[m')
    sleep(2)
