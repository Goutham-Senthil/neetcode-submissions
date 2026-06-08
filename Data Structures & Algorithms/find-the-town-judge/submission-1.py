class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [0]*(n+1)
        outdegrees = [0]*(n+1)

        for u,v in trust:
            indegrees[v] +=1
            outdegrees[u] +=1
        
        
        for i in range(1,n+1):
            if outdegrees[i] == 0 and indegrees[i] == n-1:
                return i 
    
        return -1