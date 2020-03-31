num = (int(input('Digite um numero: ')))
c = 1
v = num
while v > 0:
    print('{}'.format(v), end='')
    print(' x ' if v > 1 else print(' = '), end='')
    c = c * v
    v = v - 1
print(c, end='')