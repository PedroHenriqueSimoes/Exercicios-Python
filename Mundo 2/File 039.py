from datetime import date
genero = ((str(input('Seu genero é feminino ou masculino? '))).strip()).lower()
if genero == 'feminino':
    print('Você não irá se alistar no exercito !')
elif genero == 'masculino':
    nasc = (int(input('Qual seu ano de nascimento? ')))
    hj = date.today().year
    idade = hj - nasc
    if idade < 18:
        print('Você ainda irá se inscrever no exercito, faltam {} anos e vai ser feito em {} !'.format(18 - idade, hj - (idade - 18)))
    elif idade > 18:
        print('Você já fez o alistamento militar, em {} há {} anos atras !'.format(nasc + 18, idade - 18))
    else:
        print('Você tem que fazer o alistamento militar URGENTEMENTE !!!')
