class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = dict()
        
        for i in nums:
            if count.get(i, False):
                return i          
            count[i] = 1
