lista = list()
cont = 0
while True:
    num = (int(input('Informe um numero: ')))
    '''cont = cont + 1'''
    lista.append(num)
    resp = (str(input('Quer continuar? [S/N] '))).strip()[0]
    while resp not in 'SsNn':
        resp = (str(input('Não entendi. Quer continuar [S/N] '))).strip()[0]
    if resp in 'Nn':
        break
print('=' * 40)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros')
print(f'Os valores em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
