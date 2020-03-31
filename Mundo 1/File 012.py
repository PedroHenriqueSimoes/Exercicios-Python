preco = (float(input('\033[33mDigite o valor do produto: ')))
print('O\033[32m produto que custava {:.2f} com 5% de desconto ele ira valer {:.2f}'.format(preco, preco - ((5 / preco) * 100)))