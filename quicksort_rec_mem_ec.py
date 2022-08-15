import random

nums = [4, 1, 6, 3, 2, 7, 8]
fst = 0
lst = len(nums) - 1


def quicksort(nums, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


quicksort(nums, fst, lst)
print(nums)