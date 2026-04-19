def par_impar(array_usuario):
    par = 0
    impar = 0

    for i in range(len(array_usuario)):
        if array_usuario[i] % 2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar

def tirar_repetidos(array_usuario):
    i = 0
    while i < len(array_usuario):
        j = i + 1
        while j < len(array_usuario):
            if array_usuario[i] == array_usuario[j]:
                del array_usuario[j]
            j += 1
        i += 1
    return array_usuario

def main():
    array_usuario = []
    numeros_array = int(input("Quantos números você quer adicionar? "))

    for i in range(numeros_array):
        array_usuario.append(int(input("Digite um número: ")))
    
    par, impar = par_impar(array_usuario)

    array_usuario = tirar_repetidos(array_usuario)

    print(f"Quantidade de números pares: {par}")
    print(f"Quantidade de números ímpares: {impar}")
    print(f"Array sem repetidos: {array_usuario}")

if __name__ == "__main__":
    main()