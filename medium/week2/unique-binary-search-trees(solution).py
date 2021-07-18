class Solution:
    """
    https://leetcode.com/problems/unique-binary-search-trees/discuss/703644/PythonEasy-DP-Solution-Explained-By-Someone-Who-Used-To-Struggle-To-Understand-DP
    """
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n+1)
        self.table[0] = 1
        return self.numTreesRec(n)
        
    def numTreesRec(self, n):
        if self.table[n] != -1:
            return self.table[n]
        total = 0
        for m in range(n):
            total += (self.numTreesRec(n-1-m) * self.numTreesRec(m))
        self.table[n] = total
        return total
    
class Solution2:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i- 1 - j]
        return dp[n]
