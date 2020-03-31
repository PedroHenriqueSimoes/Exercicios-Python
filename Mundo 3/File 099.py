from time import sleep


def maior(*num):
    print('Analizando valores. . .')
    if len(num) == 0:
        print('Nenhum valor registrado')
    else:
        for n in range(0, len(num)):
            print(num[n], end=' ')
            sleep(0.3)
        print(f'Foram lidos {len(num)} valores e o maior é', end=' ')
        print(max(num))


def lin():
    print('-=' * 30)


lin()
maior(9, 2, 3, 8)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior()
