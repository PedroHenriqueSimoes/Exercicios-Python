mida = 0
agen = 0
m21 = 0
for pes in range(1, 5):
    print('{:-^40}'.format(' {}ª pessoa ! '.format(pes)))
    nome = (str(input('Qual é o nome da {}ª Pessoa? '.format(pes))))
    idade = (int(input('Quantos anos tem a {}ª Pessoa? '.format(pes))))
    genero = ((str(input('Qual o sexo da {}ª Pessoa [M / F] '.format(pes))).lower()).strip())
    if genero == 'm':
        if idade >= agen:
            agen = idade
            masc = nome
    if genero == 'f':
        if idade <= 21:
            m21 = m21 + 1
    mida = idade + mida
    print('')
print('')
print('A media de idade do grupo é de {}'.format(mida / 4))
print('O homem mais velho é {} com {} anos !'.format(masc.title(), agen))
print('{} mulheres tem menos de 21 anos'.format(m21))
