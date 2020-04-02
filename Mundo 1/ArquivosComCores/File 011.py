l = (float(input('\033[35mQual a lugura da parede? \033[m')))
a = (float(input('\033[33mQual a altura da parede? \033[m')))
area = l * a
tinta = area / 2
print("""\033[31mA parede tem {} m de altura e {} m de largura, {} m² de area e utilizara {} l de tinta para pintar-la\033[m""".format(a, l, area, tinta))