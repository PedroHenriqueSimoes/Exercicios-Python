cont = 0
while True:
    num = (int(input('Digite um valor para ver sua tabuada (para com -1 dev) ')))
    if num < 0:
        break
    cont = cont + 1
    print('-' * 20)
    for c in range(0, 11):
        x = num * c
        print(f'{num} x {c} = {x}')
    print('-' * 20)
print('Programa TABUADA Finalizado com sucesso')
