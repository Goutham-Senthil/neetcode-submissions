# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val=val)

        def traverse(node):

            # lets find where to be
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val=val)
                    return
                traverse(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val=val)
                    return
                traverse(node.right)
        
        traverse(root)
        return root
                