s = "badc"
t = "baba"
#s.length == t.length will be same always

def isIsomorphic(s, t)->bool:
    memo = {}
    for i in range(len(s)):
        if s[i] not in memo:
            memo[s[i]] = t[i]
            if s[i] in memo and t[i] in memo:
                return False
        else:
            if memo[s[i]] != t[i]:
                return False
    return True

print(isIsomorphic(s, t))