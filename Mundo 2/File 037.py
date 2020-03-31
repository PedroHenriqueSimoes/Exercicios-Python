num = (int(input('Digite um numero: ')))
print("""--- O numero digitado foi {} ---
1 - Converter para Binario
2 - Converter para Octal
3 - Converter para Hexadecimal
""".format(num))
opcao = (int(input('Digite uma das bases para conversão: ')))
if opcao == 1:
    print('{} convertido para Binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção Ivalida, tente novamente !')