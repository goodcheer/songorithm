class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = []
        
    def inorderTraversal(self, root) -> list:
        if root == None:
            return
        self.inorderTraversal(root.left)
        self.answer.append(root.val)
        self.inorderTraversal(root.right)
        return self.answer

if __name__ == '__main__':
    Tree = TreeNode(1,
                    None, TreeNode(2, 
                                   TreeNode(3, None, None), None))
    inst = Solution()
    print(inst.inorderTraversal(Tree))