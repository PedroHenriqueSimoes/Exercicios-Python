lista = list()
posma = list()
posme = list()
cont = 0
for c in range(0, 5):
    num = (int(input(f'Digite um valor na posição {c}: ')))
    lista.append(num)

'''for pm in lista:
    if pm == max(lista):
        posma.append(cont)
    elif pm == min(lista):
        posme.append(cont)
    cont = cont + 1'''
print('=' * 60)
print(f'O maior valor digitado foi {max(lista)} e sua posição foi ', end='')
for pm in lista:
    if pm == max(lista):
        posma.append(cont)
        print(cont, end='... ')
    cont = cont + 1
print(f'\nO menor valor digitado foi {min(lista)} e sua posição foi ', end='')
cont = 0
for pm in lista:
    if pm == min(lista):
        posme.append(cont)
        print(cont, end='... ')
    cont = cont + 1
