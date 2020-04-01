l = (float(input('Qual a lugura da parede? ')))
a = (float(input('Qual a altura da parede? ')))
area = l * a
tinta = area / 2
print('A parede tem {} m de altura e {} m de largura;'.format(a, l))
print('{} m² de area e utilizara {} l de tinta para pintar-la'.format(area, tinta))