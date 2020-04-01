from random import randint
pc = randint(0, 5)
user = (int(input('Memorizei um numero de 0 - 5, tente advinhar !!! NUM: ')))
if pc == user:
    print('Você advinhou, parabéns !!!')
else:
    print('Você errou, pensei no numero {}, que pena !'.format(pc))
