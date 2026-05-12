class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        top=-1
        for i in s:
            if i=='(' or i=='[' or i=='{':
                a.append(i)
                top+=1
            elif i==')':
                if top>-1:
                    if a[top]=='(':
                        a.pop()
                        top-=1
                        continue
                    else:
                        return False
                else:
                    return False
            elif i==']':
                if top>-1:
                    if a[top]=='[':
                        a.pop()
                        top-=1
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                if top>-1:

                    if a[top]=='{':
                        a.pop()
                        top-=1
                        continue
                    else:
                        return False
                else:
                    return False
        if len(a)==0:
            return True
        else:
            return False
            

        