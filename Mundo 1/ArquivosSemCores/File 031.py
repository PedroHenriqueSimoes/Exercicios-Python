km = (int(input('Qual a distância da viagem: ')))
if km <= 200:
    print('A viagem custa R${:.2f}.'.format(km * 0.50))
else:
    print('A viagem custa R${:.2f}.'.format(km * 0.45))
