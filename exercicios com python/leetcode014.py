array1 = [1, 2, 3, 4, 8, 9]
array2 = [5, 6, 7, 10]

def merge_sorted_arrays(array1, array2):
    array_merged = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array_merged.append(array1[i])
            i += 1
        else:
            array_merged.append(array2[j])
            j += 1
    array_merged.extend(array1[i:])
    array_merged.extend(array2[j:])
    return array_merged

print(merge_sorted_arrays(array1, array2))