from time import sleep


def lin(msm):
    print('=' * 60)
    print('{:^60}'.format(msm))
    print('=' * 60)
    print('\033[m')


while True:
    print('\033[30:45m', end='')
    lin('SUPORTE AO CLENTE')
    dej = (str(input('\033[30:47mInforme a bibilioteca que deseja acessar:\033[m')))
    if dej.lower() == 'sair':
        break
    print('\033[0:30:44m', end='')
    lin('PROCURANDO AJUDA')
    sleep(1)
    print('\033[7m')
    help(dej)
    print('\033[m')
