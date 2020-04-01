r1 = (int(input('Digite o comprimento da primeira reta: ')))
r2 = (int(input('Da segunda: ')))
r3 = (int(input('E da terceira: ')))
if r2 + r3 > r1 > r2 - r3 and r1 + r3 > r2 > r1 - r3 and r1 + r2 > r3 > r2 - r1:
    print('É possivel fazer um triângulo.')
else:
    print('Não é possivel fazer um triângulo.')