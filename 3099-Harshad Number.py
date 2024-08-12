'''An integer divisible by the sum of its digits is said to be a Harshad number. 
You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.'''

x=23

def HarshadNumber(x)->int:
    temp=x
    total=0
    while temp>0:
        total += temp%10
        temp = temp//10
    return total if x%total==0 else -1

print(HarshadNumber(x))