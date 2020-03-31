lista = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso....')
    else:
        print('Valor duplicado, não vou adicionar....')
    resp = (str(input('Quer continuar? [S/N] '))).strip()[0]
    while resp not in 'SsNn':
        resp = (str(input('Quer continuar? [S/N] '))).strip()[0]
    if resp in 'Nn':
        break
print('=' * 40)
lista.sort()
print(f'Os valores foram {lista}')
