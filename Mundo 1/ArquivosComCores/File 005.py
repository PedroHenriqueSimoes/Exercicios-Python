num = (int(input('\033[0;34mDigite um numero: ')))
print('\033[0;32mO numero digitado foi {},'.format(num))
print('seu sucessor é {}, e seu antecessor é {}.\033[m'.format(num + 1, num- 1))
