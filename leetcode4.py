array = [1, 2, 3, 4, 5, 20, 7, 8, 9, 10, 11]

maior_numero = array[0]

for numero in array:
    if numero > maior_numero:
        maior_numero = numero

print(maior_numero)
