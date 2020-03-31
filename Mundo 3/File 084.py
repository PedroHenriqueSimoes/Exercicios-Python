princ = list()
temp = list()
maior = menor = 0
while True:
    temp.append((str(input('Informe um nome: '))).strip().title())
    temp.append(float(input('Informe o peso: (Kg) ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] < menor:
            menor = temp[1]
        elif temp[1] > maior:
            maior = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = (str(input('Deseja continuar [S/N] '))).strip()[0]
    while resp not in 'SsNn':
        resp = (str(input('Deseja continuar [S/N] ')))
    if resp in 'Nn':
        break
print(f'Ao todo foram cadastradas {len(princ)} pessoas')
print(f'O maior peso lido foi {maior:.2f} tendo como dono: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso lido foi {menor:.2f} tendo como dono: ',end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
