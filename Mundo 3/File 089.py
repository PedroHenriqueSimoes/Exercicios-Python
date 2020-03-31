alunos = list()
tot = list()
cont = 0
pef = 0
while True:
    nome = (str(input('Informe o nome do aluno: '))).strip().title()
    alunos.append(nome)
    nota1 = (float(input('Informe a primera nota: ')))
    alunos.append(nota1)
    nota2 = (float(input('Informe a segunda nota: ')))
    alunos.append(nota2)
    tot.append(alunos[:])
    alunos.clear()
    resp = (str(input('Deseja continuar? [S/N] '))).strip()[0]
    while resp not in 'SsNn':
        resp = (str(input('Deseja continuar? [S/N] '))).strip()[0]
    if resp in 'Nn':
        break
print('=' * 40)
print('No        Nome               Media')
print('-=' * 20)
for c in tot:
    m = (tot[cont][1] + tot[cont][2]) / 2
    print('{:<8}'.format(cont), end=' ')
    print('{:<15}'.format(tot[cont][0]), end=' ')
    print('{:<15.1f}'.format(m, end=' '))
    cont = cont + 1
while pef != 999:
    pef = (int(input('Que aluno deseja ver a media? (para com 999) ')))
    print('=' * 40)
    if pef < len(tot[:]):
        print(f'Notas de {tot[pef][0]}: {tot[pef][1]}, {tot[pef][2]}')
    else:
        print('Numero invalido; Tente novamente !')
print('Finalizando....')
print(' < FIM DO PROGRAMA >')
