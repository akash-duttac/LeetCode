n = 30
count = 0
while n>=5:
    n = n//5
    count+=n
print(count)

# def factorial(n):
#             if n==0 or n==1:
#                 return 1
#             return n*factorial(n-1)

#         num = factorial(n)

#         count=0
#         while num%10==0:
#             count+=1
#             num//=10
#         return count