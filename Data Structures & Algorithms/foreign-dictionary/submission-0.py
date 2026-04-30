class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # This is a topological sort problem
        # we create a map of every charater 
        # to every character this is after it
        adj = {c:set() for w in words for c in w}

        for w1,w2 in zip(words,words[1:]):
            minLen = min(len(w1),len(w2))
            # this is a base case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # this will map a c to a 
        # boolean value
        # True -> it is being visited (in our current path) (cycle)
        # False -> it is not being visited
        visit = {}

        res  = []

        # this is a postorder DFS
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            # there is a cycle
            if dfs(c):
                return ""
        return "".join(res)[::-1]