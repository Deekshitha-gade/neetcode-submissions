class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if max(i)>=target:
                l=0
                r=len(i)-1
                while(r>=l):
                    mid=(l+r)//2
                    if i[mid]==target:
                        return True
                    elif i[mid]>target:
                        r=mid-1
                    else:
                        l=mid+1
                return False
            
            else:
                continue
        return False
                    
            
        