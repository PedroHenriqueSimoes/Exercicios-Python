a = (int(input('Digite um numero: ')))
b = (int(input('Digite outro numero: ')))
c = (int(input('Digite um ultimo numero: ')))
maior = a
menor = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

print('O maior numero é {} e o menor é {}.'.format(maior, menor))