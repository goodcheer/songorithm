class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur_node = root
        while True:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                k -= 1
                if not k:
                    break
                cur_node = cur_node.right
        return cur_node.val

if __name__ == '__main__':
    Tree = TreeNode(3,
                    TreeNode(1, None, TreeNode(2, None, None)),
                    TreeNode(4, None, None))
    k = 1
    inst = Solution()
    print(inst.kthSmallest(Tree, k))