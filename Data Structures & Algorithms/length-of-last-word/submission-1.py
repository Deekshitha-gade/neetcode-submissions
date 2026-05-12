class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=[]
        if " " not in s:
            return len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and len(a)!=0:
                return len(a)
            elif s[i]==" " and len(a)==0:
                continue 
            else:
                a.append(s[i])
        