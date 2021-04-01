# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0
        
    def pathSum(self, root, sum_):
        def dfs(root, prev):
            if not root:
                return 
            cur = prev + root.val
            if cur - sum_ in rec:
                self.cnt += rec[cur - sum_]
            if cur in rec:
                rec[cur] += 1
            else:
                rec[cur] = 1

            dfs(root.left, cur)
            dfs(root.right, cur)
            rec[cur] -= 1

        rec = {0:1}
        dfs(root, 0)
        return self.cnt
"""
Another Solution
----------------------
class SolutionBruteForce:
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target-root.val) + self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
"""