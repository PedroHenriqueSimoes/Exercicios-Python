from random import randint
cpu = randint(1, 20)
cont = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR !')
print('-=' * 20)
while True:
    num = (int(input('Digite um valor: ')))
    jog = (str(input('PAR ou IMPAR? [P/I] ')))[0].strip()
    s = num + cpu
    if jog in 'Pp':
        if s % 2 == 0:
            print('PAR ! Jogador Vence !!!!')
            cont = cont + 1
        elif s % 2 == 1:
            print('IMPAR ! Computador Vence !!!!')
            break
    elif jog in 'Ii':
        if s % 2 == 0:
            print('PAR ! Computador Vence !!!!')
            break
        elif s % 2 == 1:
            print('IMPAR ! Jogador Vence !!!!')
            cont = cont + 1
    else:
        while jog not in 'PpIi':
            jog = (str(input('PAR ou IMPAR [P/I] ')))[0].strip()
    print(f'Deu {s}')
    print(f'O computador jogou {cpu} e o jogador jogou {num}')
print(f'O jogador ganhou {cont} vezes mas....')
print('\033[31mGAME OVER')
