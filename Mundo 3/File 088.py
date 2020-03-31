from random import randint
from time import sleep
rep = list()
tot = list()
print('=' * 60)
print('{:-^60}'.format('JOGUE NA MEGACENA'))
print('=' * 60)
print('')
palp = (int(input('Quantos palpites quer tentar? P: ')))
print(f'======= Sorteando {palp} jogos =======')
sleep(1)
for c in range(0, palp):
    for i in range(0, 6):
        t = randint(1, 60)
        while t in rep:
            t = randint(1, 60)
        if t not in rep:
            rep.append(t)
            rep.clear()
            tot.append(t)
    print(f'Jogo {c + 1}: {tot}')
    tot.clear()
    sleep(1.5)
print('==========< BOA SORTE >==========')