def area(alt, larg):
    art = alt * larg
    print(f'O terreno de propriedades {alt:.1f} x {larg:.1f} tem àrea total de {art:.1f}m² ')


print('    Controle de terrenos')
print('-' * 30)
a = (float(input('LARGURA (m): ')))
l = (float(input('ALTURA (m): ')))
area(a, l)
