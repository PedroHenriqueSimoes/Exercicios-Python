r1 = (int(input('\033[34mDigite o comprimento da primeira reta: \033[m')))
r2 = (int(input('\033[33mDa segunda: \033[m')))
r3 = (int(input('\033[35mE da terceira: \033[m')))
if r2 + r3 > r1 > r2 - r3 and r1 + r3 > r2 > r1 - r3 and r1 + r2 > r3 > r2 - r1:
    print('\033[32mÉ possivel fazer um triângulo.\033[m')
else:
    print('\033[31mNão é possivel fazer um triângulo.\033[m')