def voto(id):
    from datetime import date
    hoje = date.today().year
    idade = hoje - id
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA !'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL !'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO !'


print('=' * 50) # PRG PRINC
nasc = (int(input('Em que ano você nasceu? ')))
print(voto(nasc))