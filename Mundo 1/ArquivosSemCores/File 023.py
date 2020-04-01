num = (int(input('Digite um numero: ')))
un = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print("""O numero digitado foi {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(num, un, dez, cen, mil))