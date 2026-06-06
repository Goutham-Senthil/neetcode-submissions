class Solution:
    def transpose(self, m: List[List[int]]) -> List[List[int]]:
        p = len(m)
        n = len(m[0])
        trans = [[m[j][i] for j in range(p)] for i in range(n)]
        
        return trans