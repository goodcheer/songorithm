from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col <0 or col >= len(grid[0]) or grid[row][col] != '1':
                return
            grid[row][col] = 0
            
            dfs(row + 1, col)
            dfs(row -1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt
                
if __name__ == '__main__':
    inst = Solution()
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    print(inst.numIslands(grid))