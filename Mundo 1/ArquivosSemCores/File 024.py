city = ((str(input('Digite sua cidade: '))).strip()).lower()
cstrip = city.strip()
cstrip = 'santo' in cstrip[0]
print('Começa com "Santo"? R= {}'.format(cstrip))