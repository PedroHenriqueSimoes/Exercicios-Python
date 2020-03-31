def fish(jog, gol=0):
    if jog == '':
        jog = '<desconhecido>'
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato !')


# PRG P
p = (str(input('Informe o nome do jogador: '))).strip().title()
g = (str(input('Informe a quantidade de gol(s) que ele fez no campeonato: ')))
fish(p, g)
if g.isnumeric:
    g = (int(g))
else:
    g = 0
