'''You are given an array of positive integers nums.
Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or 
all double-digit numbers from nums, and the rest of the numbers are given to Bob. 
Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.
Return true if Alice can win this game, otherwise, return false.'''

# nums = [1,2,3,4,10]
nums = [1,2,3,4,5,14]
def canAliceWin(nums)->bool:
    singleSum, doubleSum=0, 0
    for num in nums:
        if num<10:
            singleSum+=num
        else:
            doubleSum+=num
    
    return True if singleSum!=doubleSum else False

print(canAliceWin(nums))