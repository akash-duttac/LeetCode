s = "hello"

def score(s):
    nums = [ord(char) for char in s]

    i, j, sum = 0, 1, 0
    while i<j and j<len(nums):
        sum += abs(nums[i]-nums[j])
        i+=1
        j+=1
    
    return sum
# print(ascii)

print(score(s))
