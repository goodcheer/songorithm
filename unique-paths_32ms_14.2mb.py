class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if min(m, n) == 1:
            return 1
            
        grid = [[1 for _ in range(n) ] for _ in range(m)]
        print(grid)
        for i in range(1, m):
            for j in range(1, n):
                print(f"grid[{i}][{j}] <- grid[{i-1}][{j}] + grid[{i}][{j-1}]")
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[i][j]
