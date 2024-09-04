'''You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.'''

# nums = [2,1,3,5,6]
# k = 5
# multiplier = 2

# Output: [8,4,6,5,6]
# nums = [1,2]
# k = 3
# multiplier = 4
import sys
nums = [7,71,15]
k=10
multiplier = 3

def getFinalState(nums, k, multiplier):
    def getMin(nums):
        smallest = sys.maxsize
        index = -1
        for i in range(len(nums)):
            if nums[i]<smallest:
                smallest = nums[i]
                index = i
        
        return index
    
    for _ in range(k):
        index = getMin(nums)
        nums[index] *= multiplier
    
    return nums

print(getFinalState(nums,k,multiplier))