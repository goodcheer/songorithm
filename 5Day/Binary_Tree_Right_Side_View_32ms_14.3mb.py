from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = []
        
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        def bfs(nodes : List[TreeNode]) -> int:
            if not nodes:
                return
            self.answer.append(nodes[-1].val)
            tmp = []
            for node in nodes:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            return bfs(tmp)
        bfs([root])
        return self.answer

if __name__ == '__main__':
    inst = Solution()
    tree = TreeNode(1,
                    TreeNode(2,None,TreeNode(5, None, None)), 
                    TreeNode(3,None,TreeNode(4, None, None)))
    print(inst.rightSideView(tree))