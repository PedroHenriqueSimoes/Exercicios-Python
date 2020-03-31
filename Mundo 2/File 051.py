num = (int(input('Digite o primeiro termo: ')))
raz = (int(input('Qual a razão da PA? ')))
nt = 0
for pa in range(0, 10):
    num = num + raz
    print(num, end= ' > ')
print('FIM !')
