ma = 0
men = 0
mai = 0
for m in range(1, 6):
    peso = (float(input('Quanto pesa a {}º pessoa? (Kg) '.format(m))))
    if m == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi {:.1f} Kg'.format(maior))
print('O menor peso lido foi {:.1f} Kg'.format(menor))
