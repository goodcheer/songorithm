

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = []
        
        # heap, so key as value(s.t. ordered by frequency count)
        # minheap, so -freqs[f]
        
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        topk = list()
        
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
            # K번만큼 추출. 최소 힙이므로 가장 작은 음수 순으로 추출
        
        return topk
        


            
            
        