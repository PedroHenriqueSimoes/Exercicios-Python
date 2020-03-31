sex = ((str(input('Qual seu genero? [M/F] '))).strip()).upper()[0]
while sex !='M' and sex != 'F':
    sex = ((str(input('Não entendi o que digitou ! Tente outra vez [M/F] '))).strip()).upper()[0]
if sex == 'M':
    print('Sexo masculino registrado !')
else:
    print('Sexo feminino registrado !')
print('FIM !')
