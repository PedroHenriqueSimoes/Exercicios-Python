r1 = (float(input('Digite a primeira reta: ')))
r2 = (float(input('Digite a segunda reta: ')))
r3 = (float(input('Digite a terceira reta: ')))
if r2 + r3 > r1 > r2 - r3 and r1 + r3 > r2 > r1 - r3 and r2 + r2 > r3 > r1 - r2:
    print('Podem formar um triângulo ', end='')
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('escaleno !')
    elif r1 == r2 and r2 == r3:
        print('equilatero  !')
    else:
        print('isoceles !')
else:
    print('Não é possivel fazer um triângulo !')
