cont = s = num = 0
while True:
    num = (int(input('Digite um numero: (para com 999) ')))
    if num == 999:
        break
    s = s + num
    cont = cont + 1
print(f'Foram digitados {cont} numeros e a soma entre eles é {s}')
