from time import sleep
num1 = (int(input('Digite o primeiro valor: ')))
num2 = (int(input('Digite o segundo valor: ')))
menu = 0
while menu != 5:
    menu = (int(input("""
    Opções:
    
    [ 1 ] Soma
    [ 2 ] Multiplicação
    [ 3 ] Maior valor
    [ 4 ] Novos numeros
    [ 5 ] Sair
    
    Sua escolha: """)))
    if menu == 1:
        print('A soma vale {} !'.format(num1 + num2))
    elif menu == 2:
        print('A multiplicação vale {} !'.format(num1 * num2))
    elif menu == 3:
        if num1 > num2:
            print('O maior valor é {} !'.format(num1))
        elif num1 < num2:
            print('O maior valor é {} !'.format(num2))
        else:
            print('Ambos os valores são equivalentes !')
    elif menu == 4:
        num1 = (int(input('Digite o primeiro valor: ')))
        num2 = (int(input('Digite o segundo valor: ')))
    elif menu == 5:
        print('Finalizando !')
    else:
        print('Opa, ouve um erro !')
    sleep(1.5)
print('Fim do programa !')
