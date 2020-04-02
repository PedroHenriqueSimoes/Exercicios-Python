rs = (float(input('\033[32mQuantos reais? R$: \033[m')))
d = rs / 4.16
print('\033[33mCom {:.2f}R$ que você tem, da para comprar {:.2f} dolares\033[m'.format(rs, d))