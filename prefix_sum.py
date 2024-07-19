'''
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
'''

gain = [-5,1,5,0,-7]

prefix_sum = 0

for i in range(len(gain)):
    temp = 0
    for j in range(i):
        temp += gain[j]
    if temp > prefix_sum:
        prefix_sum = temp

print(prefix_sum)