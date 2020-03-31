num = ata = cont = 0
num = (int(input('Digite um numero (para com 999): ')))
while num != 999:
    ata = ata + num
    cont = cont + 1
    num = (int(input('Digite um numero (para com 999): ')))
print('Foram digitados {} numeros e soma entre eles é {}'.format(cont, ata))
