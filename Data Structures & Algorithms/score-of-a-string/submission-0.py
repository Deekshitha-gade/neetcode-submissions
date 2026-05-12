class Solution:
    def scoreOfString(self, s: str) -> int:
        absdif=0
        for i in range(1,len(s)):
            absdif+=abs(ord(s[i])-ord(s[i-1]))
        return absdif