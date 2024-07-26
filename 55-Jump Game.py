# nums = [2, 3, 1, 1, 4] # true
# nums = [3,2,1,0,4] # false
nums = [2, 0]
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

def canJump(nums):
    jump = 0
    for num in nums:
        if jump<0:
            return False
        elif num>jump:
            jump=num
        
        jump = jump-1

    return True
'''
def canJump(nums):
    i=0

    while i<len(nums):
        jump = nums[i]
        print("Jump: ", jump, " i: ", i)
        if jump==0: 
            return False
        elif i+jump<len(nums):
            i += jump 
            if i==len(nums)-1: return True
        else:
            i += len(nums)-jump
        
    
    return False
    '''

print(canJump(nums))