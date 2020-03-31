cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'anil': '\033[35m'}

n1 = (float(input('{}Digite a primeira media: '.format(cores['azul']))))
n2 = (float(input('{}{}Digite a segunda media: '.format(cores['limpa'], cores['amarelo']))))
print('{}A primeira nota foi {:.2f}, a segunda foi {:.2f}, e a media foi {:.2f}'.format(cores['anil'], n1, n2, (n1 + n2) / 2))