tupla = ((int(input('Informe um valor: '))),
    (int(input('Informe outro valor: '))),
    (int(input('Informe mais um valor: '))),
    (int(input('Informe o ultimo valor: '))))
print(f'Foram digitados {len(tupla)} numeros, sendo eles {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não apareceu.')
print('Os valores pares foram', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(f'{c}', end=' ')
    elif c % 2 == 1:
        print('.', end=' ')
