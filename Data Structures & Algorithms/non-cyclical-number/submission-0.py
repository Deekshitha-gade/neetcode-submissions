class Solution:
    def isHappy(self, n: int) -> bool:
        count=0
        a=[]
        
        while n!=1:
            temp=0
            count=0
            while n>0:
                temp=n%10
                count+=temp*temp
                n=n//10
            if count not in a:
                a.append(count)
            else:
                return False
            n=count
        return True
            
            



            
        