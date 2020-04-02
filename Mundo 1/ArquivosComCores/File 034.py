sal = (float(input('\033[33mQual é seu salario? ')))
if sal <= 1250.00:
    print("""\33[32mO salario que era de R${:.2f} passou para R${:.2f} 
    por conta de 15% no aumento.\033[m""".format(sal, ((sal * 15) / 100) + sal))
else:
    print("""\33[34mO salario que era de R${:.2f} passou para R${:.2f}
     por conta de 10%  no aumento\033[m""".format(sal, ((sal * 10) / 100)+ sal))