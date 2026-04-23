# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        stack = []
        serial = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                serial.append(str(node.val))
            elif not node:
                serial.append("N")

            if node:
                stack.append(node.right)
                stack.append(node.left)
        
        res = ",".join(serial)
        print(res)
        return res
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        n = len(data)
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i]=="N":
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
        
            return node
        root = dfs()
        return root
        