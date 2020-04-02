nome = ((str(input('\033[33mQual é seu nome? >>> \033[m'))).strip()).lower()
print("""\033[35mTem "Silva" no nome?
{}\033[m""".format('silva' in nome))