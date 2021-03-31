# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        current = root
        stack = []
        values = []
        
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                values.append(current.val)
                current = current.right
                
            else:
                break
        return values[k-1]
        
        
if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    e = TreeNode(2)
    
    a.left = b
    a.right = c
    b.right = e
    sol = Solution()
    assert sol.kthSmallest(a, 1) == 1
    print("success")
    