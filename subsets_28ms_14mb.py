from itertools import combinations
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] + [[i] for i in nums] # k=0, 1

        k = 2
        size = len(nums)
        if size == 1:
            return res
        while k < size:
            for arr in combinations(nums, k):
                res.append(list(arr))
            k += 1

        return res + [nums]