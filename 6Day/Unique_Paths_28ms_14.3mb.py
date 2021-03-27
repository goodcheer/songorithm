class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        grid = [[1] * n for _ in range(m)]
        grid[0][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]

if __name__ == '__main__':
    inst = Solution()
    m = 3
    n = 2
    print(inst.uniquePaths(m, n))