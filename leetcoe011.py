array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 15

def somaArray(array):
    soma = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == result:
                    return array[i], array[j], array[k]
    return False


def main():
    print("a soma é: ", somaArray(array))

if __name__ == "__main__":
    main()
