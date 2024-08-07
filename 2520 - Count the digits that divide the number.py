'''
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.
'''

def countDigits(num):
    temp = num
    count = 0

    while num>0:
        val = num%10
        if val != 0 and temp%val==0:
            count+=1
            print(val)
        num=num//10

    return count

print(countDigits(1248))