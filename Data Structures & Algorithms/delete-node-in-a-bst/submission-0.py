# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # What we can do is 
        # use this function recursively 
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            # we found it 
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # we wanna find  
                # the minimum from the right subtree
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val # we have now TWO instances of the "min" from right subtree
                root.right = self.deleteNode(root.right,root.val)
        return root
