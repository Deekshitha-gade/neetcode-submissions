class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=0
        y=0
        while y<len(t):
            if x==len(s):
                return True
            if s[x]==t[y]:
                y+=1
                x+=1
            else:
                y+=1
        if x!=len(s):
            return False
        return True