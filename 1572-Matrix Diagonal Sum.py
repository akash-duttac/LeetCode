'''Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal 
that are not part of the primary diagonal.
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.'''


mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

#left diagonal
# for i in range(len(mat)):
#     print(mat[i][i])
#right diagonal
# for i in range(len(mat)):
#     print(mat[i][len(mat)-1-i])

#the middle element will be added twice in odd lengths

def diagonalSum(mat):
    totalSum=0
    for i in range(len(mat)):
        totalSum += mat[i][i] #left diagonal
        totalSum += mat[i][len(mat)-1-i] #right diagonal

    #if the matrix length is odd there will be overlap
    if len(mat)%2!=0:
        totalSum -= mat[len(mat)//2][len(mat)//2]
    
    return totalSum

print(diagonalSum(mat))