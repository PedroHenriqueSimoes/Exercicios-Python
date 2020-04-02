tc = (float(input('\033[36mQuantos graus Celsus? Cº: \033[m')))
print('\033[35mTemperatura de {:.1f}Cº em fahrenheint fica {:.1f}Fº.\033[m'.format(tc, (tc / 5) * 9 + 32))