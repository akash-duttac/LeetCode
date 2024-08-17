'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]

#matrix.length = matrix[i].length = n

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # 1 - transpose of matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2 - reverse each row of matrix
        for i in range(n):
            left=0
            right=len(matrix[i])-1
            while left<right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left+=1
                right-=1
        
        print(matrix)

        return
    
obj = Solution()
obj.rotate(matrix)