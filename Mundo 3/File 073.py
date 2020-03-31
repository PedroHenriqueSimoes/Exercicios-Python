braz = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
        'Vasco DG', 'Chapecoence', 'Atlrtico-MG', 'Botafogo', 'Atletico-PR',
        'Bahia', 'São Paulo', 'Fluminence', 'Sport Recife', 'EC Vitoria',
        'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico GO')
print('=' * 260)
print('\033[4:34mLista de times do brazileirão 2017:\033[m')
print(braz)
print('=' * 260)
print('\033[4:32mOs primeros 5 colocados são:\033[m')
print(braz[0:5])
print('=' * 260)
print('\033[4:31mOs ultimos 4 colocados são:\033[m')
print(braz[-4:])
print('=' * 260)
print('\033[4:35mOs times em ordem alfabetica:\033[m')
print(sorted(braz))
print('=' * 260)
print(f'O Chapeconence esta {braz.index("Chapecoence") + 1}ª posição')