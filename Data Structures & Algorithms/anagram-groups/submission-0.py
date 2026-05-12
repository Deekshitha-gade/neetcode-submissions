class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        ans=defaultdict(list)
        fin={}
        for i in strs:
            fin[i]=0
        for i in range(n):
            l=[]
            if fin[strs[i]]==0:
                fin[strs[i]]=1 
                l.append(strs[i])        
                for j in range(i+1,n):
                    if sorted(strs[i])==sorted(strs[j]):
                        fin[strs[j]]=1
                        l.append(strs[j])
                ans[strs[i]]=l
        return ans.values()


                    

        