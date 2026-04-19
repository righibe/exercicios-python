digitos_texto = input("Digite os digitos: ")
soma = 0
tamanho = len(digitos_texto)
for i in range(tamanho):
    valor = digitos_texto[i]
    soma += int(valor)

print(soma)
