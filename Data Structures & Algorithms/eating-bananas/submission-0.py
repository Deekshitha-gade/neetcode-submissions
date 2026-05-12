class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n=1
        m=max(piles)
        res=m
        while(m>=n):
            mid=(m+n)//2
            count=0
            for i in piles:
                count+=math.ceil(i/mid)
            if count<=h:
                res=min(res,mid)
                m=mid-1
            else:
                n=mid+1
        return res


        