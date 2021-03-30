from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

if __name__ == '__main__':
    inst = Solution()
    nums = [2,0,2,1,1,0]
    inst.sortColors(nums)
    print(nums)