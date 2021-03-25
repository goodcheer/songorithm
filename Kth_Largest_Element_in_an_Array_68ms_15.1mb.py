import heapq
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        answer = 0
        for _ in range(n - k + 1):
            answer = heapq.heappop(nums)
        return answer

if __name__ == '__main__':
    inst = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(inst.findKthLargest(nums, k))