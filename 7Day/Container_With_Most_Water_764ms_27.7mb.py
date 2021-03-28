from typing import List
class Solution:
    def __init__(self):
        self.answer = 0
        
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        while left < right:
            self.answer = max(self.answer, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return self.answer

if __name__ == '__main__':
    inst = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(inst.maxArea(height))