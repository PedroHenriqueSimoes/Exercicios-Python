from random import randint
from time import sleep
from operator import itemgetter
rank = list()
jog = {'jogador1': randint(1, 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),
       'jogador4': randint(1, 6)}
for k, v in jog.items():
    print(f'O jogador {k} tirou {v}')
    sleep(0.5)
rank = sorted(jog.items(), key= itemgetter(1), reverse=True)
print('=' * 60)
print('  < RANKING > ')
for i, v in enumerate(rank):
    print(f'     Em {i + 1}º lugar ficou: {v[0]} ({v[1]} pts)')
