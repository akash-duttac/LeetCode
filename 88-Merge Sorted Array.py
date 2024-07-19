nums1 = [4,5,6,0,0,0]
m = 3 
nums2 = [1, 2, 3]
n = 3

j = 0

for i in range(m, m+n):
    nums1[i] = nums2[j]
    j+=1

for i in range(len(nums1)-1):
    if nums1[i]>nums1[i+1]:
        nums1[i], nums1[i+1] = nums1[i+1], nums1[i]

print(nums1)