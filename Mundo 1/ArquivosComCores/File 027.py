nome = ((str(input('\033[34mDigite seu nome: \033[m'))).strip()).lower()
nsplit = nome.split()
ncor = nome.title()
print("""\033[36mO nome digitado foi {}
O primeiro nome é {}
E o ultimo é {}\033[m""".format(ncor, nsplit[0].title(), nsplit[(len(nsplit)) - 1].title()))