num = (int(input('Digite um numero: ')))
tot = 0
for c in range(0, num):
    if num % (c + 1) == 0:
        print('\033[33m', end= ' ')
        tot = tot + 1
    else:
        print('\033[31m', end= ' ')

    print(c + 1, end ='')
print('', end= '\n')
print('\033[mO numero {} foi divisivel {} vezes\033[m'.format(num, tot))
if tot == 2:
    print('\033[32mÉ um numero primo !\033[m')
else:
    print('\033[31mNão é um numero primo !\033[m')