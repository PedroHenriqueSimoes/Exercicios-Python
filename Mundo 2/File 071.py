sed50 = sed20 = sed10 = sed1 = div = 0
print('=' * 40)
print('{:^40}'.format('Caixa Eletrônico'))
print('=' * 40)
vs = (int(input('Quanto deseja sacar? R$: ')))
while True:
    sed50 = vs // 50
    s = vs % 50
    sed20 = s // 20
    s = s % 20
    sed10 = s // 10
    s = s % 10
    sed1 = s // 1
    s = s % 1
    if s == 0:
        break
print('=' * 40)
print('Foram precisas ', end='')
if sed50 != 0:
    print(f'{sed50} cédulas de R$50')
if sed20 != 0:
    print(f'{sed20} cédulas de R$20')
if sed10 != 0:
    print(f'{sed10} cédulas de R$10')
if sed1 != 0:
    print(f'{sed1} cédulas de R$1')
