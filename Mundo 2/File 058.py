from random import randint
cpu = randint(0, 10)
jog = (int(input('Tente advinhar um valor de 0 - 10: ')))
tent = 1
while jog != cpu:
    if jog > cpu:
        jog = (int(input('Menos, tente outra vez: ')))
    elif jog < cpu:
        jog = (int(input('Mais, tente outra vez: ')))
    tent = tent + 1
print('Isso, pensei no numero {}, você tentou {} vezes !'.format(cpu, tent))
