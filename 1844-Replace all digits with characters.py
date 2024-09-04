s = "a1c1e1"

def replaceDigits(s: str) -> str:
    answer = ""
    for i in range(len(s)):
        if i%2 != 0:
            prev = ord(s[i-1])
            answer += chr(prev+int(s[i]))
        else:
            answer += s[i]
    return answer

print(replaceDigits(s))