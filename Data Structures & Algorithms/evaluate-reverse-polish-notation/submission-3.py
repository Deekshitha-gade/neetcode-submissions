class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=['*','+','-','%','/']
        a=[]
        for i in tokens:
            if i in s:
                b=int(a[-1])
                a.pop()
                c=int(a[-1])
                a.pop()
                if i=='+':
                    a.append(c+b)
                elif i=='-':
                    a.append(c-b)
                elif i=='*':
                    a.append(c*b)
                elif i=='/':
                    a.append(int(c/b))
                else:
                    a.append(c%b)
            else:
                a.append(i)
        return a[0]
        