from collections import Counter
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
    
if __name__ == '__main__':
    inst = Solution()
    nums = [1,3,4,2,2]
    print(inst.findDuplicate(nums))