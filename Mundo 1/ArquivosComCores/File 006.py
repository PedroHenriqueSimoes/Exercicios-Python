num = (int(input('\033[0;33mDigite um numero: \033[m')))
dob = num * 2
trip = num * 3
sqrt = num ** (1 / 2)
print('\033[35mO numero digitado foi {}'.format(num))
print('seu dobro é {}, seu triplo é {}, sua raiz quadrada é {:.2f}.\033[m'.format(dob, trip, sqrt))
