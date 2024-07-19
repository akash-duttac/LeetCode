nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(nums)
def reverse(nums, i, j):
    while i<j:
        nums[i], nums[j] = nums[j], nums[i]
        i+=1
        j-=1
    return nums

nums = reverse(nums, 0, len(nums)-1)
nums = reverse(nums, 0, k-1)
nums = reverse(nums, k, len(nums)-1)
# def right_shift(nums, k):
#     i=0
#     j=k-1
#     while i<j:
#         nums[i], nums[j] = nums[j], nums[i]
#         i+=1
#         j-=1
#     i=k
#     j=len(nums)-1
#     while i<j:
#         nums[i], nums[j] = nums[j], nums[i]
#         i+=1
#         j-=1
#     return nums

# i=0
# j=len(nums)-1

# while i<j:
#     nums[i], nums[j] = nums[j], nums[i]
#     i+=1
#     j-=1


print(nums)