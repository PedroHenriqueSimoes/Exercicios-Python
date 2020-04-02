dia = (int(input('\033[32mQuantos dias o carro ficou aluguado? \033[m')))
km = (float(input('\033[33mQuantos km foram rodados? KM: \033[m')))
print("""\033[mO carro ficou alugado por {} dias e rodou {:.1f}Km 
fica custando o total de R$ {:.2f}.""".format(dia, km, (dia * 60) + (km * 0.15)))