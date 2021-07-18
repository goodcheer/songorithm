"""
✔️ Solution 1: HashSet

    The idea is to use HashSet to track past elements.
    We iterate the combinations of nums[i], nums[j], nums[k], and calculate the last number by lastNumber = target - nums[i] - nums[j] - nums[k].
    We check if lastNumber is existed the past by checking in the HashSet, if existed, then it form a quadruplets then add it to the answer.
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans
