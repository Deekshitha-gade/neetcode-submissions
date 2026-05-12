class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def max1(prices,k,maxsum):
            n=len(prices)
            l,h=0,k-1
            while h<=n-1:
                sum=0
                for i in range(l,h+1):
                    sum=prices[h]-prices[l]
                maxsum=max(sum,maxsum)
                l+=1
                h+=1
            if k<=n-1:
                return max1(prices,k+1,maxsum)
            else:
                return maxsum
        maxsum=0
        return max1(prices,2,maxsum)
        

        