'''
You are given a 0-indexed integer array nums of even length and there is also an empty array arr. 
Alice and Bob decided to play a game where in every round Alice and Bob will do one move. 
The rules of the game are as follows:

Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
Now, first Bob will append the removed element in the array arr, and then Alice does the same.
The game continues until nums becomes empty.
Return the resulting array arr.
'''

nums = [5,4,2,3] #output [3, 2, 5, 4]

def numberGame(nums):
    #sort the array first
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]>nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    print(nums)
    
    arr=[]
    for i in range(1,len(nums), 2):
        arr.append(nums[i])
        arr.append(nums[i-1])
    return arr

print(numberGame(nums))