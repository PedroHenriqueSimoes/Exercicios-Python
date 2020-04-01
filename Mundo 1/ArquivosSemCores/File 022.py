nome = ((str(input('Digite seu nome: '))).strip()).title()
nsplit = nome.split()
njoin = ''.join(nsplit)
print("""O seu nome é {}
Maiusculo: {}
Minusculo: {}
Letras: {}
O primeiro nome tem {} letras.""".format(nome, nome.upper(), nome.lower(), len(njoin), len(nsplit[0])))