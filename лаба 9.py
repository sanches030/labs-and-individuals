import sys
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums1 = []
nums2 = [-4, -6, 4, 9]
        
def arithmetic_mean(nums):
    a = sum(nums) / len(nums)
    return a

def closest(nums):
    if len(nums) == 0:
           return("масив пустий, додайте якісь значення!")
    avg = arithmetic_mean(nums)
    closest_nums = []
    temp = nums.copy()
    for i in range(3):
        closest_num = sys.maxsize
        for element in temp:
            if abs(avg - element) < abs(avg - closest_num):
                closest_num = element
        closest_nums.append(closest_num)
        temp.remove(closest_num)
    return closest_nums

#print(closest(nums1))
print(f"{arithmetic_mean(nums)}\n{closest(nums)}")
#print(closest(nums)
