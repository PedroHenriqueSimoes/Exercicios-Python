city = ((str(input('\033[31mDigite sua cidade: \033[m'))).strip()).lower()
cstrip = city.strip()
cstrip = 'santo' in cstrip[0]
print("""\033[35mComeça com "Santo"?
{}
\033[m""".format(cstrip))