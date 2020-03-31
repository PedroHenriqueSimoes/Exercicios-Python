n1 = (float(input('Digite a primeira nota: ')))
n2 = (float(input('Digie a segunda nota: ')))
m = (n1 + n2) / 2
print('A media é {:.1f}...'.format(m))
if  6.9 < m < 5.0:
    print('RECUPERAÇÃO !')
elif m >= 7.0:
    print('APROVADO !')
elif m < 5.0:
    print('REPROVADO !')
