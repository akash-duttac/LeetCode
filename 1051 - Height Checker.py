class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        temp = heights[:]

        def merge_sort(arr):
            if len(arr)>1:
                i=j=k=0
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                merge_sort(left)
                merge_sort(right)
                while i<len(left) and j<len(right):
                    if left[i]<right[j]:
                        arr[k] = left[i]
                        i+=1
                        k+=1
                    else:
                        arr[k] = right[j]
                        j+=1
                        k+=1
                while i<len(left):
                    arr[k] = left[i]
                    i+=1
                    k+=1
                while j<len(right):
                    arr[k] = right[j]
                    j+=1
                    k+=1
            
            return arr
        
        expected = merge_sort(heights)
        count = 0
        print(expected)
        print(temp)
        for i in range(len(expected)):
            if expected[i]!=temp[i]:
                count+=1
        
        return count

obj = Solution()
a = obj.heightChecker([1,1,4,2,1,3])
print(a)
