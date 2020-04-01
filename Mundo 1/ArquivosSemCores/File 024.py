city = ((str(input('Digite sua cidade: '))).strip()).lower()
cstrip = city.strip()
cstrip = 'santo' in cstrip
print("""Começa com "Santo"?
{}
""".format(cstrip))