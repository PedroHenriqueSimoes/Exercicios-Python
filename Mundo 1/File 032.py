from datetime import date
ano = (int(input('\033[34mDigite um ano (digite 0 para o ano atual): ')))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('\033[31m{} é um ano bixesto !'.format(ano))
else:
    print('\033[33m{} não é um ano bixesto !'.format(ano))
