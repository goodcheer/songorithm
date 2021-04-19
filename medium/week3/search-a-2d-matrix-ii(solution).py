class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(mn)
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n-1
        
        while (i < m) and (j >= 0):
            current = matrix[i][j]
            if current == target:
                return True
            elif current > target: # if current is bigger than target
                j -= 1  # move current to left(smaller side)
            else:
                # if current is smaller than target
                i += 1 # move current to below (bigger side)
        return False