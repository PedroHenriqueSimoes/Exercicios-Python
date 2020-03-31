cont = 1
tot = caro = pbarato = 0
while True:
        prod = ((str(input(f'Digite o nome do {cont}º produto: '))).capitalize()).strip()
        preco = (float(input(f'Informe o preco do {cont}º produto R$: ')))
        tot = tot + preco
        if cont == 1 or preco < pbarato:
                barato = prod
                pbarato = preco
        elif preco >= 1000:
                caro = caro + 1
        cont = cont + 1
        frent = (str(input('Quer continuar? [S/N] ')))
        while frent not in 'SsNn':
                frent = (str(input('Quer continuar? [S/N] ')))
        if frent in 'Nn':
                break
print(f'Foram comprados {cont} produtos ao todo . . .')
print(f'O total gasto será R${tot:.2f}')
print(f'{caro} produtos passaram de R$1000')
print(f'O produto mais barato foi {barato} custando apenas {pbarato:.2f}')
