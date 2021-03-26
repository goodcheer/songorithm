from itertools import combinations as cb
class Solution:
    def __init__(self):
        self.answer = []
        
    def subsets(self, nums: list) -> list:
        for i in range(len(nums) + 1):
            for arr in cb(nums, i):
                self.answer.append(list(arr))
        return self.answer

if __name__ == '__main__':
    inst = Solution()
    nums = [1, 2, 3]
    print(inst.subsets(nums))