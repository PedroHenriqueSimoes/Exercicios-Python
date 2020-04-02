cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[32m',
         'anil': '\033[35m'}

num = (int(input('{}Digite um numero: '.format(cores['azul']))))
print('{}'.format(cores['amarelo']))
print(':*:' * 5)
print('TABUADA DO {}'.format(num))
print(':*:' * 5)
print('{}'.format(cores['anil']))
print(""" 
 x 1 = {}
 x 2 = {}
 x 3 = {}
 x 4 = {}
 x 5 = {}
 x 6 = {}
 x 7 = {}
 x 8 = {} 
 x 9 = {}
 x 10 = {}\033[m
 """.format(num,  num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10))
