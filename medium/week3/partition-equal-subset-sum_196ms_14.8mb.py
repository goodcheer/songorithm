class Solution:
    """using cascade """
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 != 0:
            return False
        target = tot // 2
        
        subsets = {0}
        
        for i in nums:
            subsets.update([s+i for s in subsets])
            if target in subsets:
                return True
