class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        m = len(grid)
        n = len(grid[0])
        rotten = 0
        fresh = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    rotten+=1
                    q.append((i,j))
        
        time = -1
        if fresh == 0:
            return 0

        while q:
            roundLen = len(q)
            time+=1
            for _ in range(roundLen):
                i,j = q.popleft()
            
                for n_i,n_j in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                    if 0<=n_i<m and 0<=n_j<n and grid[n_i][n_j] == 1:
                        fresh -= 1
                        grid[n_i][n_j] = 2 # rotten 
                        q.append((n_i,n_j))
        return time if fresh == 0 else -1

