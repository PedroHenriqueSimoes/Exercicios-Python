nome = ((str(input('Digite seu nome: '))).strip()).lower()
nsplit = nome.split()
ncor = nome.title()
print("""O nome digitado foi {}
O primeiro nome é {}
E o ultimo é {}""".format(ncor, nsplit[0].title(), nsplit[(len(nsplit)) - 1].title()))