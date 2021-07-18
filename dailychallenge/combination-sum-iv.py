class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            # print(f"=========dp[{i}]===========")
            for x in nums:
                # print(x)
                if x <= i:
                    # print(f"dp[{i}](={dp[i]}) += dp[{i-x}](={dp[i-x]})")
                    dp[i] += dp[i - x] 
                    # print(dp)
        return dp[target]
        
 
if __name__ == '__main__':
    sol = Solution()
    assert sol.combinationSum4(nums=[1,2,3], target=4) == 7