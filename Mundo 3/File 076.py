produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo',
            25.00, 'Transferidor', 4.20, 'Copasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('=' * 48)
print('{:^50}'.format('\033[1mLISTAGEM DE PREÇOS\033[m'))
print('=' * 48)
cont = 0
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:<15}', end='')
    else:
        print(f'R$ {produtos[item]:.>30.2f}')
