# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # pre-order traversal
        node = root
        stack = []
        path = []
        
        while True:
            if node is not None:
                path.append(node)
            if node is not None:
                stack.append(node.right)
                node = node.left
            elif stack:
                node = stack.pop()
            else:
                break
        
        n = len(path)
        for i in range(n-1):
            path[i].left = None
            path[i].right = path[i+1]
        return
            
