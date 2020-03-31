print('{:>^40}'.format(' LOJAS BRAZILEIRAS '))
preco = (float(input('Qual o preço das suas compras? R$: ')))
form = (int(input("""Qual forma de pagamento?
1 - A vista no dinheiro
2 - A vista no cheque
3 - A vista no cartão
4 - 2x no cartão
5 - 3x  ou mais no cartão
Qual a opção? # """)))
if form == 1 or form == 2:
    print('Você ganhou 10% de desconto, agora o produto custa R${:.2f} !'.format(preco -((preco * 10) / 100) ))
elif form == 3:
    print('Você ganhou 5% de desconto, agora o produto custa R${:.2f} !'.format(preco - ((preco * 5) / 100)))
elif form == 4:
    print('O preço foi dividido em  2 parcelas de R${:.2f}, obrigado pela preferência !'.format(preco / 2))
elif form == 5:
    parc = (int(input('Quantas parcelas? # ')))
    juros = ((preco * 20) / 100) + preco
    print('Parcelando em {}x de R${:.2f} e com juros de 20%, o produto custa agora R${:.2f} !'.format(parc, juros / parc, juros))
else:
    print("""\033[31mOcorreu um erro :(
 >>> Verifique se você escreveu tudo certinho !""")
