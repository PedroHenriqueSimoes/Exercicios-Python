preco = (float(input('\033[33mDigite o valor do produto: \033[m')))
print("""O\033[32m produto que custava {:.2f} com 5 por cento de desconto
 ira valer {:.2f}\033[m""".format(preco, preco - ((5 / preco) * 100)))