import random

nums = [4, 1, 6, 3, 2, 7, 8]


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = random.choice(nums)
        low_nums = [n for n in nums if n < pivot]
        upp_nums = [n for n in nums if n > pivot]
        equ_nums = [n for n in nums if n == pivot]

        return quicksort(low_nums) + equ_nums + quicksort(upp_nums)


print(quicksort(nums))