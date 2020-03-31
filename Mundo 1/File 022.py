nome = ((str(input('\033[34mDigite seu nome: '))).strip()).title()
nsplit = nome.split()
nsplit = ''.join(nsplit)
print("""\033[33mO seu nome é {}
Maiusculo: {}
Minusculo: {}
Letras: {}
O primeiro nome tem {} letras.""".format(nome, nome.upper(), nome.lower(), len(nsplit), len(nome[0])))