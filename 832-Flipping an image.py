'''Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].'''

image = [[1,1,0],[1,0,1],[0,0,0]] #[[1,0,0],[0,1,0],[1,1,1]]

def flipAndInvertImage(image):
    for row in image:
        #reverse the row
        left=0
        right=len(row)-1
        while left<right:
            row[left], row[right] = row[right], row[left]
            left+=1
            right-=1
    ans=[]
    for row in image:
        r=[]
        for num in row:
            x=1 if num==0 else 0
            r.append(x)
        ans.append(r)
    
    return ans

print(flipAndInvertImage(image))