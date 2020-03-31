dados = dict()
totg = list()
cont = gol = 0
dados['nome'] = (str(input('Informe o nome do jogador: '))).strip().title()
part = (int(input('Informe a quantidade de partidas do jogador: ')))
for c in range(1, part + 1):
    gols = (int(input(f'Quantos gols foram marcados no {c}ª partidada? ')))
    totg.append(gols)
dados['gols'] = totg.copy()
print('=' * 50)
print(f'O jogador {dados["nome"]} jogou {part} partidas no total: ')
for t in range(1, part + 1):
    print('   =>', f'Na {t}ª partida {dados["nome"]} fez {dados["gols"][cont]} gols')
    cont = cont + 1
for c in dados['gols']:
    gol = gol + c
print(f'Foi um total de {gol} gols !')
