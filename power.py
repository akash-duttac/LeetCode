def myPow(x, n, memo = {}) -> float:
    if n==0:
        return 1.0
    if n in memo:
        return memo[n]
    else:
        memo[n] = x*myPow(x, n-1)
        return memo[n]
    
print(myPow(2, 1024))
# print(myPow(2, -2))