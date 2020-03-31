num = (int(input('Digite um numero: ')))
print('{:=^40}'.format(' TABUADA DO {} '.format(num)))
for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num * c))