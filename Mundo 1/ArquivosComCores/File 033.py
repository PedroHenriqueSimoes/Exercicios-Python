a = (int(input('\033[35mDigite um numero: \033[m')))
b = (int(input('\033[34mDigite outro numero: \033[m')))
c = (int(input('\033[36mDigite um ultimo numero: \033[m')))
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

print('\033[32mO maior numero é {} e o menor é {}.\033[m'.format(maior, menor))