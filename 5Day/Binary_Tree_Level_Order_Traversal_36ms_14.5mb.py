from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = []
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = [root]
        while stack:
            tmp = []
            res= []
            for cur_node in stack:
                if cur_node:
                    res.append(cur_node.val)
                    tmp.append(cur_node.left)
                    tmp.append(cur_node.right)
            if res:
                self.answer.append(res)
            stack = tmp[:]
        return self.answer

if __name__ == '__main__':
    inst = Solution()
    tree = TreeNode(3,
                    TreeNode(9,None,None), 
                    TreeNode(20,TreeNode(15, None, None),TreeNode(7, None, None)))
    print(inst.levelOrder(tree))