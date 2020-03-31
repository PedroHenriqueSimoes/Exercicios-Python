#SOLUÇÃO DO GUANABARÁ APERFEIÇOADA
num = [[], [], []]
for c in range(1, 8):
    n = (int(input(f'Informe o {c}º valor: ')))
    num[2].append(n)
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
num[2].sort()
print(f'Os valores encontrados foram {num[2]}')
print(f'Os valores pares foram {num[0]}')
print(f'E os impares foram {num[1]}')

# MINHA SOLUÇÃO 1
'''lista = list()
pares = list()
impares = list()
for c in range(1, 8):
    num = (int(input(f'Digite o {c}º numero: ')))
    lista.append(num)
lista.sort()
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f"""Os numeros digitados foram: {lista}
Os numeros pares foram: {pares}
Os numeros impares foram: {impares}""")'''


# MINHA SOLUÇÃO 2

'''lista = list()
for c in range(1, 8):
    num = (int(input(f'Digite o {c}º numero: ')))
    lista.append(num)
lista.sort()
print(f'Os numeros diitados foram: {lista}')
print(f'Os valores pares foram: ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
print(f'\nOs valores impares foram: ', end='')
for n in lista:
    if n % 2 == 1:
        print(n, end=' ')'''
