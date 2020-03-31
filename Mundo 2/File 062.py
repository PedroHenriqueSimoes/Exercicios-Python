term = 1
num = (int(input('Digite o primeiro valor: ')))
raz = (int(input('Digite a razão: ')))
count = 0
sus = 0
while count != 10:
    count = count + 1
    num = num + raz
    print('> {} '.format(num), end='')
while term != 0:
    print('')
    term = (int(input('Queantos termos a mais (0 encerra):')))
    sus = 0
    while sus != term:
        num = num + raz
        print('> {} '.format(num), end= '')
        count = count + 1
        sus = sus + 1
print('A progreção foi finalizada com {} termos !'.format(count))
