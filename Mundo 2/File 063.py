n = (int(input('Digite a quantidade de digitos de Fibocelli: ')))
count = 0
num1 = 0
sla = 1
print('\033[4:34mOs primeros {} digitos de Fibocelli são:\033[m')
print('1 >', end='')
while count != n - 1:
    count = count + 1
    num2 = sla
    sla = num1 + num2
    print(' {} >'.format(sla), end='')
    num1 = num2
print(' FIM')
