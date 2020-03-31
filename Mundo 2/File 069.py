cont = 1
m18 = m20 = hr = 0
while True:
    idade = (int(input(f'Informe a idade da {cont}ª pessoa: ')))
    if idade > 18:
        m18 = m18 + 1
    sexo = (str(input(f'Informe o sexo da {cont} pessoa: [M/F] ')))[0].strip()
    while sexo not in 'MmFf':
        sexo = (str(input(f'Digite o sexo da {cont}ª pessoa: [M/F] ')))[0].strip()
    if sexo in 'Mm':
        hr = hr + 1
    if sexo in 'Ff':
        if idade <= 20:
            m20 = m20 + 1
    cont = cont + 1
    rep = (str(input('Quer continuar? [S/N]')))[0].strip()
    if rep in 'Nn':
        break
    while rep not in 'SsNn':
        rep = (str(input('Quer continuar [S/N]')))[0].strip()
    print('~' * 40)
print(f'Foram registradas {cont} pessoas . . .')
print(f'{m18} pessoas passaram dos 18 anos.')
print(f'Foram registrados {hr} homens ao todo')
print(f'E {m20} mulheres com menos de 20 anos')
