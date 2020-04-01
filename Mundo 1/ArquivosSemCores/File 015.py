dia = (int(input('Quantos dias o carro ficou aluguado? ')))
km = (float(input('Quantos km foram rodados? KM:')))
print('O carro ficou alugado por {} dias e rodou {:.1f}Km'.format(dia, km))
print('Seu custo será de {:.2f} R$.'.format((dia * 60) + (km * 0.15)))