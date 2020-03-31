from uteis import moeda

p = (float(input('Informe um preço: R$')))
d = ' '
t = bool()
while d not in 'SsNn':
    d = (str(input('Deseja deixar formatado para dinheiro? [S/N] '))).strip()[0]
    if d in 'Ss':
        t = True
        break
    if d in 'Nn':
        t = False
        break
print(f'A metade do preço é {moeda.metade(p, t)}')
print(f'O dobro do preço é {moeda.dobro(p, t)}')
print(f'Aumentando 10% fica {moeda.aumentar(p, 10, t)}')
print(f'Diminuindo 13% fica {moeda.diminuir(p, 13, t)}')