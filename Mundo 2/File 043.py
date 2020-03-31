alt = (float(input('Quanto você mede? (M) ')))
peso = (float(input('Quanto você pesa? (Kg) ')))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('Você esta abaixo do peso !')
elif 18.5 <= imc < 25.0:
    print('Peso ideal !')
elif 25.0 <= imc < 30.0:
    print('Sobrepeso !')
elif 30.0 <= imc < 40.0:
    print('Obesidade !')
elif imc >= 40.0:
    print('Obesidade Morbida, cuidado !')
print('O seu IMC: {:.1f}'.format(imc))