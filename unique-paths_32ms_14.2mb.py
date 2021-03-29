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

    
if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(1, 7) == 1
    assert sol.uniquePaths(199, 1) == 1
    print("success")
