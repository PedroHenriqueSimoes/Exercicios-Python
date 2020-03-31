from File115.lib.Interfarce import cab

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Ouve um erro na criação do arquivo !')
    else:
        print('Arquivo "pessoas.txt"criado com sucesso !')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo !')
    else:
        cab('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mOuve um erro !\033[m')
    else:
        try:
            a.write(f'{nome} {idade}\n')
        except:
            print('\033[31mOuve um erro ao escrever no arquivo\033[m')
        else:
            print(f'Registro de {nome} criado com sucesso !')


