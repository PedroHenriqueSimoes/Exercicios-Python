km = (float(input('\033[35mQual a velocidade atual? KM: \033[m')))
if km > 80:
    print('\033[31mVocê foi multado ! A multa custa R$ {:.2f}.\033[m'.format((km - 80) * 7))
else:
    print('\033[32mDesculpe, tenha um bom dia e dirija com segurança !\033[m')