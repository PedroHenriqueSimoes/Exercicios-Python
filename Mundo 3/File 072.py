tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'cartoze', 'quinze',
        'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
resp = 'Ss'
while resp in 'Ss':
    num = (int(input('Digite um numero de 0 - 20: ')))
    while 0 > num or num > 20:
        num = (int(input('Tente novamente. Digite um numero de 0 - 20: ')))
    print(f'O numero digitado foi {tupla[num]} !')
    resp = (str(input('Quer continuar? [S/N] '))).strip()[0]
    while resp not in 'SsNn':
        resp = (str(input('Quer continuar? [S/N] '))).strip()[0]
    if resp in 'Nn':
        break
print('PROGRAMA FINALIZADO')
