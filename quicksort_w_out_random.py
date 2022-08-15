nums = [4, 1, 6, 3, 2, 7, 8]


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[len(nums) // 2]  # без модуля random

        low_nums = []
        upp_nums = []
        equ_nums = []
        for n in nums:
            if n < pivot:
                low_nums.append(n)
            elif n > pivot:
                upp_nums.append(n)
            else:
                equ_nums.append(n)
        return quicksort(low_nums) + equ_nums + quicksort(upp_nums)


print(quicksort(nums))