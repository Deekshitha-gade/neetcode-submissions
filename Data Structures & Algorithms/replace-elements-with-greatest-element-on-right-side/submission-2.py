class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxn=-1
      
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i]
            arr[i]=maxn
            maxn=max(maxn,temp)
        return arr