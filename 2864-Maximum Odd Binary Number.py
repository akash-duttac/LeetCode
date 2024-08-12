'''You are given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number 
is the maximum odd binary number that can be created from this combination.
Return a string representing the maximum odd binary number that can be created from the given combination.
Note that the resulting string can have leading zeros.'''

s = "0101" 
# "1001"

def maximumOddBinaryNumber(s):
    count1 = 0
    count0 = 0
    ans = ""
    for char in s:
        if char=='1':
            count1+=1
        else:
            count0+=1

    if count1==1:
        ans = '0'*count0+"1"
        return ans
    
    ans = '1'*(count1-1) + '0'*count0 + '1'
    return ans


print(maximumOddBinaryNumber(s))