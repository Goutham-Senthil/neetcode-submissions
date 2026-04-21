# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def Same(r1,r2):

            if not r1 and not r2:
                return True

            
            elif r1 and r2 and r1.val == r2.val:
                return Same(r1.right,r2.right) and Same(r1.left,r2.left)
            else:
                return False
        
        ans = Same(p,q)
        return ans