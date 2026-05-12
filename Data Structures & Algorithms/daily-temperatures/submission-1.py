class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n=len(temperatures)
        res=[]
        for i in range(n):
            if i<n-1:
                count=1
            else:
                count=0
            for j in range(i+1,n):
                if temperatures[i]>=temperatures[j]:
                    if j<n-1 and i<n-1:
                        count+=1
                        continue
                    else:
                        count=0
                        break
                else:
                    break
            res.append(count)
        return res
