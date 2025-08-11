cid = str(input('Qual seu nome completo?')).strip()
r = cid.upper()
if 'SILVA' in r:
    print('parece que sua cidade tem Silva no nome!')
else:
    print('parece que sua cidade nao tem Silva no nome!')