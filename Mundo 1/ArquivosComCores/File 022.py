nome = ((str(input('\033[34mDigite seu nome: \033[m'))).strip()).title()
nsplit = nome.split()
njoin = ''.join(nsplit)
print("""\033[33mO seu nome é {}
Maiusculo: {}
Minusculo: {}
Letras: {}
O primeiro nome tem {} letras.\033[m""".format(nome, nome.upper(), nome.lower(), len(nsplit), len(nsplit[0])))