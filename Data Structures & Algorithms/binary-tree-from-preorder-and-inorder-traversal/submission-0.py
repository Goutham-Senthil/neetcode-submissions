# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def builder(preorder,inorder):
            # Base case nothing
            if not preorder or not inorder:
                return None
            
            # root of a given tree/subtree is present at 0th index 
            # of a preorder traversal
            # Preorder is N->L->R
            root = TreeNode(preorder[0])
            
            # inorder is L-> N -> R
            node_index = inorder.index(preorder[0])
            root.left = builder(preorder[1:node_index+1],inorder[:node_index+1])
            root.right = builder(preorder[node_index+1:],inorder[node_index+1:])
            return root
        
        return builder(preorder,inorder)