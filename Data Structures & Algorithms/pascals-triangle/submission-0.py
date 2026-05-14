class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return res
        else:
            for i in range(3,numRows+1):
                temp=[1]
                for i in range(len(res[-1])-1):
                    temp.append(res[-1][i]+res[-1][i+1])
                temp.append(1)
                res.append(temp)
                
        return res
