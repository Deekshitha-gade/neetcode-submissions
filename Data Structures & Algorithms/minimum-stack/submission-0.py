class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        n=len(self.stack)-1
        return self.stack[n]
    
        

    def getMin(self) -> int:
        return min(self.stack)
        
