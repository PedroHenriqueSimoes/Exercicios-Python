pes = list()
dados = dict()
fem = list()
acima = list()
soma = 0
while True:
    dados['nome'] = ((str(input('Informe um nome: '))).strip().title())
    dados['sexo'] = (str(input('Informe o sexo: [M/F] '))).strip()[0]
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = (str(input('Informe o sexo: [M/F] '))).strip()[0]
    if dados['sexo'] in 'Ff':
        fem.append(dados['nome'])
    dados['idade'] = (int(input('Informe a idade: ')))
    resp = (str(input('Deseja continuar? [S/N] '))).strip()[0]
    pes.append(dados.copy())
    while resp not in 'SsNn':
        resp = (str(input('Deseja continuar? [S/N]')))
    if resp in 'Nn':
        break
print('=' * 40)
for i in range(0, len(pes)):
    soma = soma + pes[i]['idade']
for p in pes:
    if p['idade'] >= soma / len(pes):
        acima.append(p['nome'])
print(f'Foram cadastradas {len(pes)} pessoas')
print(f'A media de idade do grupo é de {soma / len(pes):.2f}')
print(f'Lista das mulheres registradas: {fem}')
print(f'Lista das pessoas acima da média: {acima}')
print('=' * 40)
