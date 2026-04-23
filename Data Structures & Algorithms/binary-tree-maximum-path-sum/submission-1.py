# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_res = [-1001]

        def path(node):
            if not node:
                return 0
            

            max_left = path(node.left)
            max_right = path(node.right)
            leftMax = max(0,max_left)
            rightMax = max(0,max_right)
            sum_value = node.val + leftMax + rightMax
            max_res[0] = max(max_res[0],sum_value)

            return node.val + max(leftMax,rightMax)
        
        path(root)
        return max_res[0]

