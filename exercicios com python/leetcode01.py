array = [3, 3]
target = 6

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] + array[j] == target:
            print(i, j)
            break
    else:
        continue
    break

print(len(array))