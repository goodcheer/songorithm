class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#recursive solution
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))

if __name__ == '__main__':
    inst = Solution()
    tree = TreeNode(3,
                    TreeNode(2,None,TreeNode(3, None, None)), 
                    TreeNode(3,None,TreeNode(1, None, None)))
    print(inst.rob(tree))