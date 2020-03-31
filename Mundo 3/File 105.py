def notas(*n, show=False):
    """
     -> Função que lê varias notas e retorna um dicionario com dados
    :param n: Lê varias notas (numero indefinido)
    :param show: Mostra a situação do aluno (opc)
    :return: Retorna um dicionario
    """
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n)/dados['total']
    if show:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA !'
        elif 7 > dados['media'] > 5:
            dados['situação'] = 'RAZOAVEL !'
        elif dados['media'] <= 5:
            dados['situaçãos'] = 'RUIM !'
    return dados

user = list()
t = bool()
while True:
    user.append(float(input('Informe uma nota: ')))
    resp = ' '
    while resp not in 'SsNn':
        resp = (str(input('Deseja continuar: [S/N] '))).strip()[0]
        if resp in 'Ss':
            break
        if resp in 'Nn':
            break
        print('\033[31m:<errozin>: Informe apenas os valores S ou N !\033[m')
    if resp in 'Nn':
        break
most = ' '
while most not in 'SsNn':
    most = (str(input('Deseja mostra a situação? [S/N] '))).strip()[0]
    if most in 'Ss':
        t = True
        break
    elif most in 'Nn':
        t = False
        break
    print('\033[31m:<errozin>: Informe apenas os valores S ou N ! \033[m')

tot = (notas(user, show=t))
print(tot)
