from random import randint
tupla = (randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados', end=' ')
cont = 0
#Modo do Guanabará
for c in tupla:
    print(tupla[cont], end=' ')
    cont = cont + 1
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')

#Meu modo:
'''
for c in range:
    print(tupla[cont, end=' ')
    if cont == 0:
            menor = tupla[0]
            maior = tupla[0]
        else:
            if maior < tupla[cont]:
                maior = tupla[cont]
            if menor > tupla[cont]:
                menor = tupla[cont]
        cont = cont + 1
print('')
print(f'O maior valor lido foi {maior}')
print(f'O menor valor lido foi {menor}')'''
