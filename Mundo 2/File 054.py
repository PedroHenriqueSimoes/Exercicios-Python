from datetime import datetime
ma = 0
me = 0
for c in range(0, 7):
    nasc = (int(input('Quando nasceu a {}º pessoa? '.format(c + 1))))
    idade = (datetime.today().year) - nasc
    if idade >= 21:
        ma = ma + 1
    else:
        me = me + 1
print('{} pessoas já são maiores de idade !'.format(ma))
print('enquanto {} não são...'.format(me))
