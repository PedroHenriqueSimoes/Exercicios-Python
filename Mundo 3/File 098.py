from time import sleep


def cont(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -(passo)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.0)
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c},', end=' ')
            sleep(0.3)
    elif inicio > fim:
        for c in range(inicio, fim - 1, -passo):
            print(f'{c},', end=' ')
            sleep(0.3)
    sleep(0.3)
    print('FIM !')


def lin():
    print('-=' * 30)


# CODIGO PRINCIPAL

lin()
cont(1, 10, 1)
lin()
cont(10, 0, 2)
lin()
print('Agora é sua vez de iniciar a contagem !')
i = (int(input('Informe um inicio: ')))
f = (int(input('Informe um final:  ')))
p = (int(input('Informe o passo:   ')))
lin()
cont(i, f, p)
print('< FIM DO PROGRAMA >')
