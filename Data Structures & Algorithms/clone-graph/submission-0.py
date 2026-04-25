"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:

        if not root:
            return root
        
        m = {}

        def dfs(node):
            if node in m:
                return m[node]
            
            copy = Node(node.val)
            m[node] = copy
            for neis in node.neighbors:
                copy.neighbors.append(dfs(neis))
            return copy
        
        return dfs(root)
