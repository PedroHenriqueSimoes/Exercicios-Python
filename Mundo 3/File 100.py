from random import randint
from time import sleep
numsort = list()


def sort():
    numsort.clear()
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        numsort.append(randint(1, 10))
    for n in numsort:
        print(n, end=' ')
        sleep(0.5)
    print('Pronto !')
    sleep(1)


def addPar(*n):
    soma = 0
    for i in numsort:
        if i % 2 == 0:
            soma = i + soma
    print(f'A soma dos valores pares de {numsort}, temos {soma}')


# PROGRAMA PRINCIPAL

sort()
addPar()
