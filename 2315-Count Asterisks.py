'''You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. 
In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.
'''

# s = "l|*e*et|c**o|*de|" #always even number of vertical bars
# s = "iamprogrammer"
s = "yo|uar|e**|b|e***au|tifu|l"
def countAsterisk(s):
    count=0
    bars=0
    for x in s:
        if x=='|': bars+=1
        elif x=='*' and bars%2==0: count+=1

    return count

print(countAsterisk(s))