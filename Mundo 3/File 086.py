matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num = (int(input(f'Informe um valor para [{l, c}]: ')))
        matriz[l][c] = num
print('=' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ', end=' ')
    print()











'''print(f' [ {matriz[lont][cont]} ] ')
pos = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
dig = list()
for c in range(0, 9):
    num = (int(input(f'Digite um valor para {pos[c]}: ')))
    dig.append(num)
print('=' * 30)
print(f"""[  {dig[0]}  ] [  {dig[1]}  ] [  {dig[2]}  ]
[  {dig[3]}  ] [  {dig[4]}  ] [  {dig[5]}  ]
[  {dig[6]}  ] [  {dig[7]}  ] [  {dig[8]}  ]""")'''
