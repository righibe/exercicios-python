nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    mapa = {}

    for i in range(len(nums)):
        num = nums[i]
        complemento = target - num

        if complemento in mapa:
            return [mapa[complemento], i]

        mapa[num] = i

print(two_sum(nums, target))