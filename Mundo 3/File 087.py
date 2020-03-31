matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = (int(input(f'Informe o valor [{c, l}]: ')))
        matriz[l][c] = num
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
    soma = soma + matriz[l][2]
    print()
maior = max(matriz[1][0], matriz[1][1], matriz[1][2])
print('=' * 30)
print(f'A soma dos valores pares vale {pares}')
print(f'A soma dos valores da 3ª coluna vale {soma}')
print(f'O maior valor da 2ª coluna vale {maior}')
