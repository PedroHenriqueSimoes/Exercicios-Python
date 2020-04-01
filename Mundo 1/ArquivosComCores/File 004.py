cores = {'limpa': '\033[m',
        'vermelho': '\033[0;31m',
         'verde': '\033[0;32m',
         'amarelo': '\033[0;33m',
         'azul': '\033[0;34m',
         'anil': '\033[0;35m',
         'ciano': '\033[0;36m'}
alg = (input('{}Digite algo na tela: '.format(cores['azul'])))
print('Foi digitado "{}"::'.format(alg))
print('')
print(type(alg))
print('{}É alfabetico: {}'.format(cores['vermelho'], cores['limpa']))
print(alg.isalpha())
print('{}É numerico:{}'.format(cores['anil'], cores['limpa']))
print(alg.isnumeric())
print('{}É alfanumerico:{}'.format(cores['verde'], cores['limpa']))
print(alg.isalnum())
print('{}É escrito em maiusculas:{}'.format(cores['amarelo'], cores['limpa']))
print(alg.isupper())
print('{}É escrito em minusculas:{}'.format(cores['ciano'], cores['limpa']))
print(alg.islower())