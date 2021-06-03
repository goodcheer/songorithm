from typing import List


class Solution:

    def dfs(self, nums, path):
        if len(nums) == 0:
            self.res.append(path)
            # return , backtrack
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res