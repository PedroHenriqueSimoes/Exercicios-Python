import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib:
    print('\033[31mO site esta inacesivel !\033[m')
else:
    print('\033[32mSite pronto para ser usado !\033[m')
    print(site.read())