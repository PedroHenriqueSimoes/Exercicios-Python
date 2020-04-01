km = (int(input('\033[35mQual a distância da viagem: ')))
if km <= 200:
    print('\033[34mA viagem custa R${:.2f}.'.format(km * 0.50))
else:
    print('\033[36mA viagem custa R${:.2f}.'.format(km * 0.45))
