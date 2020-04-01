preco = (float(input('Digite o valor do produto: ')))
print('O produto custava {:.2f}'.format(preco))
print('com 5 por cento de desconto ele ira valer {:.2f}'.format(preco - ((5 / preco) * 100)))