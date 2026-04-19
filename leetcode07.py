array = [1 ,1 , 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

i = 0
while i < len(array):
    j = i + 1
    while j < len(array):
        if array[i] == array[j]:
            del array[j]
        else:
            j += 1
    i += 1

print(array)
