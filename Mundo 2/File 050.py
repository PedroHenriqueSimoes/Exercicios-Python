mult = 0
s = 1
count = 0
for sec in range(0, 6):
    num = (int(input('Digite o {}º Numero: '.format(sec + 1))))
    if num % 2 == 0:
        mult = mult + num
    count = 1 + count
print('Foram lidos {} valores e a soma deles é {}'.format(count, mult))
