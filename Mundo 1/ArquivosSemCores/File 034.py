sal = (float(input('Qual é seu salario? ')))
if sal <= 1250.00:
    print('O salario que era de R${:.2f} passou para R${:.2f}'.format(sal, ((sal * 15) / 100) + sal))
    print('por conta de 15 por cento de aumento.')
else:
    print('O salario que era de R${:.2f} passou para R${:.2f}'.format(sal, ((sal * 10) / 100)+ sal))
    print('por conta de 10 por cento de aumento')