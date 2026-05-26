"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper = {}

        def copyer(node):
            if not node:
                return None
            if node in mapper:
                return mapper[node]
            
            copyNode = Node(node.val)
            mapper[node] = copyNode
            copyNode.next = copyer(node.next)
            copyNode.random = copyer(node.random)
            
            return copyNode
            
        
        return copyer(head)