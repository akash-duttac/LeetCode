class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n, memo={}):
            if n==0: return 1
            if n==1: return x
            if n in memo: return memo[n]
            if n%2==0:
                half = pow(x, n//2)
                return half*half
            half = pow(x, n//2)
            memo[n] = half
            return x*half*half
        if n<0:
            x = 1/x
            n = -n
        return pow(x,n)