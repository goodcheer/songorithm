class Solution:
  # https://backtobackswe.com/platform/content/the-change-making-problem/video
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for x in coins:
                if x <= i:
                    dp[i] = min(dp[i], dp[i - x] + 1)
        return -1 if dp[amount] > amount else dp[amount]
            
        
