nome = ((str(input('\033[33mQual é seu nome? '))).strip()).lower()
print("""\033[35mTem "Silva" no nome?
{}""".format('silva' in nome))