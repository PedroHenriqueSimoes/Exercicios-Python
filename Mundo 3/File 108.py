from uteis import moeda

p = (float(input('Informe um preço: R$')))
print(f'A metade do preço é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro do preço é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% fica {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13% fica {moeda.moeda(moeda.diminuir(p, 13))}')