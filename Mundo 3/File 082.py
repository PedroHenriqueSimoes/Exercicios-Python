normal = list()
while True:
    num = (int(input('Digite um numero: ')))
    normal.append(num)
    resp = (str(input('Deseja continuar? [S/N] '))).strip()[0]
    while resp not in 'SsNn':
        resp = (str(input('Não entendi. Deseja continuar [S/N] ')))
    if resp in 'Nn':
        break
pares = list()
impares = list()
for c in normal:
    if c % 2 == 0:
        pares.append(c)
    elif c % 2 == 1:
        impares.append(c)
print(f'Foram digitados os numeros {normal}')
print(f"""Os numeros pares lidos são {pares}
Os numeros impares lidos são {impares}""")
