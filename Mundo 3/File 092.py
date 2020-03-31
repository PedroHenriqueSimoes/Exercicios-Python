from datetime import datetime
hoje = datetime.today().year
dados = dict()
dados['nome'] = (str(input('Informe seu nome: '))).strip().title()
dados['nasc'] = (int(input('Informe sua data de nascimento (somente o ano) ')))
dados['ctps'] = (int(input('Informe o valor da sua carteira de trabalho (0 anula): ')))
if dados['ctps'] != 0:
    dados['ctr'] = (int(input('Digite o ano de contratação: ')))
    dados['sal'] = (float(input('Informe seu salario em reais R$: ')))
    apos = hoje - dados['ctr']
else:
    apos = -1
idade = hoje - dados['nasc']
print('=' * 60)
print(f'O nome do usuario cadastrado é {dados["nome"]}')
print(f'A idade do usuario foi arrendondada como {idade}')
if dados['ctps'] != 0:
    print(f'A CTPS (Carteira de Trabalho) tem valor {dados["ctps"]}')
    print(f'O salario do usuario equivale à R$ {dados["sal"]:.2f}')
    print(f'A data de contratação foi em {dados["ctr"]}')
    if apos > 35:
        print(f'A aposentadoria ja aconteceu !')
    else:
        print(f'E tem {apos} anos de colaboração, faltando {35 - apos} anos para se aponsentar')
        print(f'aposentadoria irá ocorrer quando o usario alcançar {idade + (35 - apos)} anos de idade!')
else:
    print(f'A CTPS (Carteira de Trabalho) não foi registrada')