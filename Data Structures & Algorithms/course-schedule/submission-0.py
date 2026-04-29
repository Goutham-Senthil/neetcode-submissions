class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}

        for u,v in prerequisites:
            adj_list[u].append(v)

        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if not adj_list[crs]: # no prerequistes required
                return True
            
            visit.add(crs)
            for pres in adj_list[crs]:
                if not dfs(pres):
                    return False
            visit.remove(crs)
            # just in case some future course needs this we dont need to 
            # loop again
            adj_list[crs] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True