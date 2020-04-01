km = (float(input('Qual a velocidade atual? KM: ')))
if km > 80:
    print('Você foi multado ! A multa custa {:.2f}!'.format((km - 80) * 7))
else:
    print('Desculpe, tenha um bom dia e dirija com segurança !')