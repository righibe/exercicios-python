f = input('digite uma frase muita boa!').strip().upper()
q = f.count('A')
pp = (f.find('A')+1)
up = (f.rfind('A')+1)

print('o A aparece {} vezes, sendo primeiro na posição de número{} e o último na posição de número {} '.format(q, pp, up))
print (len(f))