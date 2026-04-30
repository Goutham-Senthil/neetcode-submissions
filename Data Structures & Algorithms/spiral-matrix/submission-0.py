class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = n 
        top = 0 
        bottom = m 

        while l<r and top <bottom:
            for i in range(l,r):
                res.append(matrix[top][i])
            top+=1

            for i in range(top,bottom):
                res.append(matrix[i][r-1])
            r-=1

            if not (l<r and top<bottom):
                break

            for i in reversed(range(l,r)):
                res.append(matrix[bottom-1][i])
            bottom-=1

            for i in reversed(range(top,bottom)):
                res.append(matrix[i][l])
            l+=1
        return res