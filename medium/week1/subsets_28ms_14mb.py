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
    
    
class Solution2:
    """recursion"""
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
