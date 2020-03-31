from uteis import numeros

def lin(tam = 42):
    return '=' * tam


def cab(txt, tam=42):
    print(lin())
    print(txt.center(tam))
    print(lin())


def menu(lst):
    cab('MENU PRINC')
    cont = 1
    for i in lst:
        print(f'\033[33m{cont} - \033[34m{i}\033[m')
        cont += 1
    opc = numeros.LeiaInt('\033[32mSua escolha:\033[m ')
    return opc
