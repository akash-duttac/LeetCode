s = "Let's take LeetCode contest"
def reverseWords(s):
    left=0
    s = list(s)

    for right in range(len(s)):
        if s[right]==" " or right==len(s)-1:
            start, end = left, right-1
            if right==len(s)-1:
                end = right
            while start<end:
                s[start], s[end] = s[end], s[start]
                start+=1
                end-=1
            left = right + 1
    
    return "".join(s)

print(reverseWords(s))