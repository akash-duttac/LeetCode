'''
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

'''
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
# Output: "this is a secret"

def decodeMessage(key, message):
    #create mappings
    cipher = {}
    start = 97
    for char in key:
        if char!=' ' and char not in cipher:
            cipher[char] = chr(start)
            start+=1
        
    decoded_message = ""
    for char in message:
        if char in cipher:
            decoded_message+=cipher[char]
        else:
            decoded_message+=char
    
    return decoded_message

print(decodeMessage(key, message))