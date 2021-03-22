from itertools import permutations as pm
class Solution:
    def permute(self, nums: list) -> list:
        return [list(arr) for arr in pm(nums, len(nums))]

if __name__ == '__main__':
    inst = Solution()
    exam1 = [1, 2, 3]
    exam2 = [0, 1]
    exam3 = [1]
    print(inst.permute(exam1))
    print(inst.permute(exam2))
    print(inst.permute(exam3))