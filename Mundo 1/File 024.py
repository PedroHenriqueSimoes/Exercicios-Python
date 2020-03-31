city = ((str(input('\033[31mDigite sua cidade: '))).strip()).lower()
cstrip = city.strip()
cstrip = 'santo' in cstrip
print("""\033[35mComeça com "Santo"?
{}
""".format(cstrip))