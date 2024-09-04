# arr = [3,0,1,1,9,7]
# a = 7
# b = 2
# c = 3

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
'''A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c'''
def countGoodTriplets(arr, a, b, c):
    answer = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                    answer+=1
    
    return answer

print(countGoodTriplets(arr, a, b, c))