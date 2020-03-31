num = (int(input('Digite o primeiro valor: ')))
raz = (int(input('Digite a razão: ')))
count = 0
while count != 10:
    count = count + 1
    num = num + raz
    print('> {} '.format(num), end='')
print('')
print('FIM !')
