r1 = (int(input('\033[34mDigite o comprimento da primeira reta: ')))
r2 = (int(input('\033[33mDa segunda: ')))
r3 = (int(input('\033[35mE da terceira: ')))
if r2 + r3 > r1 > r2 - r3 and r1 + r3 > r2 > r1 - r3 and r1 + r2 > r3 > r2 - r1:
    print('\033[32mÉ possivel fazer um triângulo.')
else:
    print('\033[31mNão é possivel fazer um triângulo.')