import random

n1 = input ('me fale um nome')
n2 = input ('me diga outro nome')
n3 = input ('me diga outro nome')
n4 = input ('me diga outro nome')
n5 = input ('me diga outro nome')
n6 = input ('me diga outro nome')

nr = [n1, n2, n3, n4, n5, n6]

rn = random.choice(nr)

while True:
    pp = input ('me fale um dos nomes récem escritos:')
    if pp == rn:
        print("parabéns você ganhou o jogo!!")
        break
    else:
        print ("resposta errada, tente novamente")

print("jogo encerrado!")