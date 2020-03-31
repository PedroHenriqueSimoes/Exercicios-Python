dados = dict()
dados['aluno'] = (str(input('Nome do aluno: '))).strip().title()
dados['media'] = (float(input(f'Media de {dados["aluno"]}: ')))
print('-=' * 30)
if dados['media'] >= 7.0:
    dados['situação'] = 'APROVADO'
elif 5.0 <= dados['media'] < 7.0:
    dados['situação'] = 'RECUPERAÇÃO'
else:
    dados['situação'] = 'REPROVADO'
print(f"""Nome do aluno: {dados['aluno']}
Media de {dados['aluno']}: {dados['media']}
Situação: {dados['situação']}""")
