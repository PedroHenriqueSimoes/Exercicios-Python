from random import randint
from time import sleep
acao = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
joj = (int(input("""Suas opções:
0 - Pedra
1 - Papel 
2 - Tesoura
Você escolhe: """)))
print('\033[7:30mJO  \033[m')
sleep(1)
print('\033[7:30mKEN \033[m')
sleep(1)
print('\033[7:30mPO! \033[m')
print('\033[32m-=\033[35m' * 20)
if cpu == 0:
    if joj == 0:
        print('Ouve um EMPATE !')
    elif joj == 1:
        print('O jogador GANHOU !')
    elif joj == 2:
        print('O computador GANHOU !')
    else:
        print('Ué, o que cê tentou???')
elif cpu == 1:
    if joj == 0:
        print('O computador GANHOU !')
    elif joj == 1:
        print('Ouve um EMPATE !')
    elif joj ==2:
        print('O jogador GANHOU !')
    else:
        print('Ué, o que cê tentou???')
elif cpu == 2:
    if joj == 0:
        print('O jagador GANHOU !')
    elif joj == 1:
        print('O computador GANHOU !')
    elif joj == 2:
        print('Ouve um IMPATE !')
    else:
        print('Ué, o que cê tentou???')
print('\033[m')
print('O jogador escolheu {} !'.format(acao[joj]))
print('O computador escolheu {} !'.format(acao[cpu]))
print('\033[32m-=' * 20)