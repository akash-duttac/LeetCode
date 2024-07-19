'''
    Input: s = "the sky is blue"
    Output: "blue is sky the"
'''
s = "the sky is blue"
#trying to reverse the string

end = len(s)
start = len(s)
space = len(s)

while start < end:
    if s[start] == ' ':
        