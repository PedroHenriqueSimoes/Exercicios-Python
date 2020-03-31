casa = (float(input('Quanto custa a casa? R$: ')))
sal = (float(input('Qual o salario do comprador? R$:')))
ano =(int(input('Quantos anos de financiamento? ')))
prest = casa / (ano * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, ano, prest))
min = ((sal * 30) / 100)
if prest <= min:
    print('Emprestimo pode ser concedido !')
else:
    print('Emprestimo Negado !')
