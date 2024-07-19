# nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
memo = {}

for num in nums:
    if num in memo.keys(): memo[num] += 1
    else: memo[num] = 1

maximum = 0
ans = 0

for key, value in memo.items():
    if value > maximum and value > len(nums)/2:
        maximum = value
        ans = key

print(ans)
