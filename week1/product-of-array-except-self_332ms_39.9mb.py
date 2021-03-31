import numpy as np


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        baseline = np.prod(nums)
        res = []
        for i in range(len(nums)):
            val = nums[i]

            if val == 0:
                prod = np.prod(nums[:i] + nums[i+1:])
            else:
                prod = baseline // val
            res.append(prod)
        return res