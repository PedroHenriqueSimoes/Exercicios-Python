s = 0
count = 0
for num in range(1, 500, 2):
    if num % 3 == 0:
        s += num
        count = count + 1
print('A soma dos multiplos de 3 de 1 até 500 (todos os {}) é {}.'.format(count, s))
