# brute force
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        return [0] + [bin(i).count("1") for i in range(1, num)]


# better solution with O(n) time/space complexity

class OptSolution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
