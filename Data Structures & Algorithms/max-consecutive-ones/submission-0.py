class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=r=0
        
        maxi=0
        while l<=r and r<len(nums):
            if nums[r]==1:
                r+=1
            else:
                print(nums[l:r])
                maxi=max(maxi,r-l)
                r+=1
                l=r
        maxi=max(maxi,r-l)       
        return maxi