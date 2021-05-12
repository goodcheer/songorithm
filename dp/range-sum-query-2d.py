class NumMatrixBruteForce:
    """Brute Force 
    
    Time complexity : O(mn)O(mn) time per query. Assume that m and n represents the number of rows and columns respectively, 
    each sumRegion query can go through at most m×n elements.
    
    """

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for col in self.mat[row1:row2+1]:
            s += sum(col[col1:col2+1])
        return s
      
 Class NumMatrixCache:
    """
    https://leetcode.com/problems/range-sum-query-2d-immutable/solution/
    
    Complexity analysis

    Time complexity : O(1) time per query, O(mn) time pre-computation. The pre-computation in the constructor takes O(mn) time. Each sumRegion query takes O(1) time.

    Space complexity : O(mn). The algorithm uses O(mn) space to store the cumulative region sum.
    """
    def __init__(self, matrix: List[List[int]]):
        nr, nc = len(matrix), len(matrix[0])
        if nr == 0 or nc == 0:
            return
        dp = [[0 for _ in range(nc+1)] for _ in range(nr+1)]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] + matrix[r][c] - dp[r][c]
                
                """
                If we want to maintain sums in dp array like this, ??? -> should have sum of all 4 elements, clearly 
                cell4 = cell4 + (cell2 + cell3 - cell1) 
                         [
                             [   (0,0)            (0,0) + (0,1)   ],
                             [   (0,0)+(1,0)            ???       ]
                         ]
                
                """
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
      
