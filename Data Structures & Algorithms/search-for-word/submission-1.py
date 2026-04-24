class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        def backtrack(r,c,index):

            if (r<0 or r>=m or c<0 or c>=n or board[r][c]!=word[index]):
                return False

            if index == len(word) - 1:
                return True
            
            index+=1

            tmp = board[r][c]
            board[r][c] = '#'
            for r_off , c_off in [(1,0),(0,1),(-1,0),(0,-1)]:
                if backtrack(r+r_off,c+c_off,index):
                    return True
            
            board[r][c] = tmp
            
            return False
        

        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        return False