nome = ((str(input('\033[34mDigite seu nome: '))).strip()).lower()
nsplit = nome.split()
ncor = nome.title()
print("""\033[36mO nome digitado foi {}
O primeiro nome é {}
E o ultimo é {}""".format(ncor, nsplit[0].title(), nsplit[(len(nsplit)) - 1].title()))