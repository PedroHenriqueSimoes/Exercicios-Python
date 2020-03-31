lista = list()
for c in range(0, 5):
    num = (int(input('Digite um numero: ')))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        cont = 0
        while cont < len(lista):
            if num < lista[cont]:
                lista.insert(cont, num)
                print(f'Adicionado na posição {cont}')
                break
            cont = cont + 1
print(f'A lista em ordem crescente é {lista}')
