from time import sleep
jog = dict()
dados = list()
gols = list()
g = list()
totg = list()
cont = tot = 0
while True:
    jog['nome'] = (str(input('Informe o nome do jogador: '))).strip().title()
    jog['part'] = (int(input(f'Informe a quantidade de partidadas que {jog["nome"]} jogou: ')))
    for c in range(1, jog["part"] + 1):
        gol = (int(input(f'Quantos gols {jog["nome"]} fez na {c}ª Partida: ')))
        gols.append(gol)
        tot = tot + gol
    g.append(gols[:])
    gols.clear()
    totg.append(tot)
    jog['total'] = totg.copy()
    resp = (str(input('Deseja continuar? [S/N] '))).strip()[0]
    dados.append(jog.copy())
    tot = 0
    while resp not in 'SsNn':
        resp = (str(input('Deseja continuar? [S/N] '))).strip()[0]
    if resp in 'Nn':
        break
print(dados, g)
print('=' * 60)
print('{:<5}'.format('cod'), end='')
print('{:<20}'.format('nome'), end='')
print('{:<10}'.format('gols'), end='')
print('tot')
print('-' * 60)
for i in dados:
    print('{:<5}'.format(cont), end='')
    print('{:<20}'.format(i['nome']), end='')
    print(g[cont], end='')
    print('{:>10}'.format(i['total'][cont]))
    cont = cont + 1
cont = 0
while True:
    esc = (int(input('Deseja visulizar os dados de qual jogador? (para com 999) ')))
    if esc == 999:
        break
    if len(dados) - 1 < esc:
        print(f'ERRO, jogador {esc} não foi registrado, tente novamente')
    else:
        for c in range(1, dados[esc]['part'] + 1):
            print(f'O jogador {dados[esc]["nome"]} fez {g[esc][cont]} gols na {cont + 1}ª partida')
            cont = cont + 1
            sleep(0.5)
    cont = 0
print('<FIM DO PROGRAMA>')
print('Obrigado por usar o TwoFutbol !')