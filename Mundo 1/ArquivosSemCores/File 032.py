from datetime import date
ano = (int(input('Digite um ano (digite 0 para o ano atual): ')))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('{} é um ano bixesto !'.format(ano))
else:
    print('{} não é um ano bixesto !'.format(ano))
