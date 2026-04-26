class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        m = len(heights)
        n = len(heights[0])

        
        ## Pacific

        Pq = deque()

        Pset = set()
        
        ## Add all pacific tiles
        for i in range(m):
            Pq.append((i,0))
            Pset.add((i,0))

        for j in range(1,n):
            Pq.append((0,j))
            Pset.add((0,j))

        ## Atlanic

        Aq = deque()
        Aset = set()

        for i in range(m):
            Aq.append((i,n-1))
            Aset.add((i,n-1))
        
        for j in range(n-1):
            Aq.append((m-1,j))
            Aset.add((m-1,j))



        ## BFS
        def BFS(q,seen):
            while q:
                x,y = q.popleft()
                for i_off,j_off in [[1,0],[0,1],[-1,0],[0,-1]]:
                    r,c = x + i_off , y+j_off
                    if 0<=r<m and 0<=c<n and heights[r][c]>=heights[x][y] and (r,c) not in seen:
                        q.append((r,c))
                        seen.add((r,c))
            return
        
        BFS(Aq,Aset)
        BFS(Pq,Pset)


        return list(Pset.intersection(Aset))