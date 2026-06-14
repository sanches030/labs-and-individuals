nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(nums):
    i = 0
    num_sum = 0
    while (i < len(nums)):
        num_sum += nums[i]
        i += 1
        if i % 5 == 0:
            nums.insert(i, num_sum)
            num_sum = 0
            i += 1
func(nums)
print(nums)