num1 = (int(input('\033[0;32mDigite um numero: \033[m')))
num2 = (int(input('\033[0;34mDigite outro: \033[m')))
print('\033[0;33mA soma entre {} e {} é \033[0;31m{}\033[m'.format(num1, num2, (num1 + num2)))