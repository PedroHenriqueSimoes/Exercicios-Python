sal = (float(input('\033[33mQual é seu salario? ')))
sf = (( sal * 15) / 100) + sal
print("""\033[35mO salario que era de R${}, com 15 por cento de aumento, 
passou a valer com R${}\033[m""".format(sal, sf))

