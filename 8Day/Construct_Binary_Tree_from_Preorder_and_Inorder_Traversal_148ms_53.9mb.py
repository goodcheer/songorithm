from collections import deque
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #preorder = val, left, right
        #inorder = left, val, right
        preorder = deque(preorder[:])
        def create_tree(preorder, inorder) -> TreeNode:
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(val = inorder[idx])
                root.left = create_tree(preorder, inorder[:idx])
                root.right = create_tree(preorder, inorder[idx + 1:])
                return root
        return create_tree(preorder, inorder)

if __name__ == '__main__':
    inst = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    inst.buildTree(preorder, inorder)
        