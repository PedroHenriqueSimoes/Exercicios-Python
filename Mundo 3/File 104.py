def leiaInt(msm):
    while True:
        n = (str(input(msm)))
        if n.isnumeric():
            return n
        print('\033[31m<errozin>\033[m')


num = leiaInt('Informe um numero: ')
print(f'O numero digitado foi {num}')
