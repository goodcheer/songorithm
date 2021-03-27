import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        
        for _ in range(k-1):
            heapq.heappop(heap)
        return -heap[0]
            
        # return sorted(nums)[-k]
            
