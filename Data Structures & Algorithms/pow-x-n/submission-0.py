class Solution:
    def myPow(self, x: float, n: int) -> float:
        power=1.00000
        if n>0:
            for i in range(n):
                power*=x
        elif n==0:
            return power
        elif n<0:
            for i in range((-n)):
                power*=(1/x)
        return power
        
        


        