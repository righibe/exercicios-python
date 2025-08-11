import random
import emoji

numero_secreto = random.randint(1, 10)
tentativas = 0

print(emoji.emojize("Tente adivinhar o número entre 1 e 10. Você pode tentar até acertar :earth_americas!" ))

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Acertou! Você precisou de {tentativas} tentativas. ")
        break
    elif palpite < numero_secreto:
        print("Muito baixo. Tente de novo.")
    else:
        print("Muito alto. Tente de novo.")