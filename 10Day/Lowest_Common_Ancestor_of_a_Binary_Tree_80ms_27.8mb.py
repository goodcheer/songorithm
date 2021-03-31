class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = None
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root):
            if not root:
                return 0
            l = search(root.left)
            r = search(root.right)
            
            #if this code run in local, root -> root.val
            if root in [p, q]:
                m = 1
            else:
                m = 0
            
            if l + r + m == 2:
                self.answer = root
                
            return l or r or m

        search(root)
        return self.answer

if __name__ == '__main__':
    inst = Solution()
    p = 5
    q = 4
    tree = TreeNode(3,
                    TreeNode(5,
                            TreeNode(6, None, None),
                            TreeNode(2,
                                     TreeNode(7, None, None),
                                     TreeNode(4, None, None))), 
                    TreeNode(1,
                            TreeNode(0, None, None),
                            TreeNode(8, None, None)))
    print(inst.lowestCommonAncestor(tree, p, q))