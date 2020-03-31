frase = ((str(input('Digite uma frase: '))).strip()).upper()
pal = frase.split()
tudj = ''.join(pal)
inv = ''
for letra in range((len(tudj)) -1, -1, -1):
    inv += tudj[letra]
print('A frase digitada foi {} e o inverso dela é {}'.format(tudj, inv))
if tudj == inv:
    print('É um palindromo !')
else:
    print('Não é um palindromo !')
