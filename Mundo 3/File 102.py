def fat(n=0, show=False):
    """
     > > > Fatorial
    :param n: Escolha um numero que deseja fazer o fatorial
    :param show: (Opc)Um valor boleano em que True mostra o processo de calculo e False retorna o valor
    :return: : Retorna a você o valor do fatorial de :n:
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    print(f)


num = (int(input('Informe um numero: ')))
most = ' '
t = bool()
while most not in 'SsNn':
    most = (str(input('Deseja informar o processo matematico? [S/N] ')))
    if most in 'Ss':
        t = True
        break
    elif most in 'Nn':
        t = False
        break
    print('\033[31mERRO ! Informe apenas S ou N ! \033[m')
fat(num, t)
