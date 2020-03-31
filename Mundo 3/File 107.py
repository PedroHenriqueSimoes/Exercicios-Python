from uteis import moeda

p = (float(input('Informe um preço: R$')))
print(f'A metade do preço é {moeda.metade(p)}')
print(f'O dobro do preço é {moeda.dobro(p)}')
print(f'Aumentando 10% fica {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13% fica {moeda.diminuir(p, 13)}')