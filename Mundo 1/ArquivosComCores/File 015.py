dia = (int(input('\033[32mQuantos dias o carro ficou aluguado? ')))
km = (float(input('\033[33mQuantos km foram rodados? KM:')))
print('O carro ficou alugado por {} dias e rodou {:.1f}Km custando o total de {:.2f} R$.'.format(dia, km, (dia * 60) + (km * 0.15)))