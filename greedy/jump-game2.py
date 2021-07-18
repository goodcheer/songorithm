"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3732/
"""
class Solution:
    n = 0
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        self.n += 1
        for i, max_jump in enumerate(nums):
            if (i + max_jump) >= len(nums)-1:
                self.jump(nums[:i+1])
                return self.n
                
