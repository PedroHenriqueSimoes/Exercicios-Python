nome = ((str(input('Qual é seu nome? '))).strip()).lower()
print("""Tem "Silva" no nome?
{}""".format('silva' in nome))