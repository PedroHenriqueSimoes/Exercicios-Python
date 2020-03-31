num1 = (int(input('\033[0;32mDigite um numero: ')))
num2 = (int(input('\033[0;34mDigite outro: ')))
print("""\033[0;33mA soma entre \033[0;32m{}\033[0;33m e \033[0;34m{}\033[0;33m 
é \033[0;31m{}""".format(num1, num2, (num1 + num2)))