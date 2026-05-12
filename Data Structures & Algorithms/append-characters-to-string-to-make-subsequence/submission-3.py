class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        x=0
        y=0
        if len(s)==1 and len(t)==1:
            if s==t:
                return 0
            else:
                return 1
        while y<len(s):
            if x==len(t):
                break
            if s[y]==t[x]:
                y+=1
                x+=1
            else:
                y+=1
        print(t[x:])
        if x<=len(t)-1:
            return len(t)-x
        else:
            return 0


