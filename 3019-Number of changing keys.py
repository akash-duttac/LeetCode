def countKeyChanges(s: str) -> int:
    s_lower = ''
    for char in s:
        if char >= 'A' and char <='Z':
            s_lower += chr(ord(char)+32)
        else:
            s_lower += char
    
    count=0
    for i in range(1, len(s_lower)):
        if s_lower[i-1]!=s_lower[i]:
            count+=1
    return count

print(countKeyChanges("aAbBcC"))