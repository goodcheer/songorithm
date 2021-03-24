from collections import Counter
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        return [n[0] for n in Counter(nums).most_common(k)]

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    inst = Solution()
    print(inst.topKFrequent(nums, k))