class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stri=""
        for i in digits:
            stri+=str(i)
        x=int(stri)
        x=x+1
        a=[]
        while x>0:
            temp=x%10
            a.append(temp)
            x=x//10
        return a[::-1]
        