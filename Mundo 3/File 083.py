ex = (str(input('Digite uma expessão: ')))
pil = list()
for s in ex:
    if s == '(':
        pil.append('(')
    elif s == ')':
        if len(pil) > 0:
            pil.pop()
        else:
            pil.append(')')
            break
if len(pil) == 0:
    print('Expressão valida')
else:
    print('Expressão invalida')
'''num = (str(input('Digite uma expressão: ')))
pd = num.count('(')
pe = num.count(')')
if pd == pe:
    print('Expressão valida')
else:
    print('Expressão invalida')'''