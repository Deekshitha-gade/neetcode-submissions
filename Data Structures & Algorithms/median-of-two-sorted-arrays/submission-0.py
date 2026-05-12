class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=[]
        num.extend(nums1)
        num.extend(nums2)
        num.sort()
        l=0
        h=len(num)-1
        mid=(h+l)//2
        if len(num)%2!=0:
            return num[mid]
        else:
            return (num[mid] +num[mid+1])/2

        