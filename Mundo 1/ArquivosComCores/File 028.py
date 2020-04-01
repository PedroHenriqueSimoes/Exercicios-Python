from random import randint
pc = randint(0, 5)
user = (int(input('\033[36mMemorizei um numero de 0 - 5, tente advinhar !!! NUM: ')))
if pc == user:
    print('\033[32mVocê advinhou, parabéns !!!')
else:
    print('\033[31mVocê errou, pensei no numero {}, que pena !'.format(pc))
