class Solution:
    def myPow(self, x: float, n: int) -> float:
        power=1.00000
        if n>0:
            for i in range((n//2)):
                power*=x
            if n%2==0:
                return power*power
            else:
                return power*power*x
        elif n==0:
            return power
        else:
            for i in range((-n//2)):
                power*=(1/x)
            if n%2==0:
                return power*power
            else:
                return power*power*(1/x)


        


        