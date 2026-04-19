string = input("Digite uma string: ")
vogais = 0
for i in range(len(string.lower())):
    if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
        vogais += 1

print(vogais)

