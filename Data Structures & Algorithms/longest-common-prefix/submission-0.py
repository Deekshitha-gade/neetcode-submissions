class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s=strs[0]
        
        while True:
            flag=True
            for i in strs:
                if s not in i:
                    s=s[:-1]
                    flag=False
            if flag==True:
                break
                
        return s