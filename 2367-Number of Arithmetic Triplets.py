'''You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

Example 1:
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. '''

# nums = [4,5,6,7,8,9]
# diff = 2    # Output: 2

nums = [0,1,4,6,7,10]
diff = 3    # Output: 2

def arithmeticTriplets(nums, diff):
    size = len(nums)
    count = 0
    for i in range(size):
        for j in range(i+1,size):
            for k in range(j+1, size):
                if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                    count+=1
    
    return count

print(arithmeticTriplets(nums, diff))