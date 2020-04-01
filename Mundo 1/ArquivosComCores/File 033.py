a = (int(input('\033[35mDigite um numero: ')))
b = (int(input('\033[34mDigite outro numero: ')))
c = (int(input('\033[36mDigite um ultimo numero: ')))
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

print('\033[32mO maior numero é {} e o menor é {}.'.format(maior, menor))