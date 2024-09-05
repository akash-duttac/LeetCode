matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def searchMatrix(matrix, target):
    lr, hr, lc, hc = 0, len(matrix)-1, 0, len(matrix[0])-1

    while lr<=hr:
        mid_r = lr + (hr-lr)//2
        if matrix[mid_r][0]<=target<=matrix[mid_r][hc]:
            while lc<=hc:
                mid_c = lc+(hc-lc)//2
                if matrix[mid_r][mid_c] == target:
                    return True
                elif matrix[mid_r][mid_c]<target:
                    lc = mid_c+1
                else:
                    hc = mid_c-1
        elif matrix[mid_r][0]<target: 
            lr = mid_r+1
        else:
            hr = mid_r-1
    
    return False

print(searchMatrix(matrix, target))