# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return (True,1)
            
            leftV,leftH = height(node.left)
            rightV,rightH = height(node.right) 

            # if node.val == 3:
            #     print(f"left side {leftV} and {leftH} ")
            #     print(f"left side {rightV} and {rightH} ")

            if leftV and rightV and max(rightH,leftH) <= min(rightH,leftH)+1:
                return (True,max(rightH,leftH)+1)
            else:# it doesnt matter
                return (False,-1)
        return height(root)[0]