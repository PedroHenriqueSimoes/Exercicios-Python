frase = ((str(input('Digite uma frase: '))).strip()).lower()
fcert = frase.capitalize()
print("""A frase digitada foi {}
A letra "A" aparece {} vezes
Apareceu na primeira vez na posição {}
e na ultima na posição {}""".format(fcert, frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))