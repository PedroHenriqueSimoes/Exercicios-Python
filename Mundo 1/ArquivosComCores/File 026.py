frase = ((str(input('\033[31mDigite uma frase: \033[m'))).strip()).lower()
fcert = frase.capitalize()
print("""\033[37mA frase digitada foi {}
A letra "A" aparece {} vezes
Apareceu na primeira vez na posição {}
e na ultima na posição {}\033[m""".format(fcert, frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))