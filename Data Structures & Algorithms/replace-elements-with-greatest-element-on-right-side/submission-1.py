class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxn=-1
        temp=maxn
        for i in range(len(arr)-1,-1,-1):
            if i==len(arr)-1:
                temp=arr[i]
                arr[i]=-1
                
            else:
                temp=arr[i]
                arr[i]=maxn
            if maxn<temp:
                maxn=temp
        return arr