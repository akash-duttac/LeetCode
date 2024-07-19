class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == '':
            return True

        index = 0
        # iterate through 's', add pointer to 't'
        for i in t:
            if i == s[index]:
                index += 1
                if index == len(s):
                    return True

        return False