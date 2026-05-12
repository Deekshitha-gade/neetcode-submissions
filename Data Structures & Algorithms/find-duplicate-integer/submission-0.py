class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        l=list({k:v for (k,v) in d.items() if v > 1})
        for i in l:
            return i
        
        