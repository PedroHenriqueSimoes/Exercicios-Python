resp = 'S'
ata = 0
cont = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = (int(input('Digite um numero: ')))
    ata = num + ata
    resp = (str(input('Quer continuar? [S/N] ')))[0].strip()
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    cont = cont + 1
print("""A media dos valores vale: {:.2f}
O maior valor lido vale: {}
O menor valor lido vale: {} """.format(ata / cont, maior, menor))