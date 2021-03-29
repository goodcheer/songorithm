class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.tmp = None
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.tmp
        root.left = None
        self.tmp = root

if __name__ == '__main__':
    inst = Solution()
    tree = TreeNode(1,
                    TreeNode(2,TreeNode(3, None, None),TreeNode(4, None, None)), 
                    TreeNode(5,None,TreeNode(6, None, None)))
    inst.flatten(tree)