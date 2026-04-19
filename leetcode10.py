array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def crescenteOuNao(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                return False
    return True

def main():
    print(crescenteOuNao(array))

if __name__ == "__main__":
    main()