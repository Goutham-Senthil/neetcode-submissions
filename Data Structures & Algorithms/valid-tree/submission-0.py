class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        if not n:
            return True
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit = set()

        def dfs(i,prev):
            if i in visit:
                return False

            visit.add(i)
            for nei in adj_list[i]:
                if nei == prev:
                    continue
                if not dfs(nei,i):
                    return False
            return True
        
        return dfs(0,-1) and len(visit) == n