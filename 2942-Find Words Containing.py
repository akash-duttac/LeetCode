words = ["abc","bcd","aaaa","cbc"]
x = "a"
def x_in_word(x, word):
    flag = False
    for char in word:
        if char==x:
            flag = True
    return True if flag==True else False

def findWords(words, x):
    arr = []
    for i in range(len(words)):
        if x_in_word(x, words[i])==True:
            arr.append(i)

    return arr

print(findWords(words, x))