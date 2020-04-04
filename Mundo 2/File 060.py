num = (int(input('Digite um numero: ')))
c = 1
v = 1
while v <= num:
    print('{}'.format(v), end='')
    print(' x ' if v != num else print(' = '), end='')
    c = c * v
    v = v + 1
print('{}'.format(c), end='')