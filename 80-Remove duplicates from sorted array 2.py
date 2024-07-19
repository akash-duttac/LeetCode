nums = [0,0,1,1,1,1,2,3,3]
# nums = [1,1,1,2,2,3]

def removeDuplicates(nums: list[int]):
    if len(nums)<=2:
        print(nums)
    
    index = 2
    for i in range(2,len(nums)):
        if nums[i]!=nums[index-2]:
            nums[index]=nums[i]
            index+=1
    
    print(nums[:index])
    print(index)

print(nums)
removeDuplicates(nums)
