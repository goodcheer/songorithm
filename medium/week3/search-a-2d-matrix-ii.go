func searchMatrix(matrix [][]int, target int) bool {
    var m, n, i, j int
    m = len(matrix)
    n = len(matrix[0])
    
    i = 0
    j = n-1
    
    for (i < m) && (j >= 0) {
        current := matrix[i][j]
        if current == target {
            return true
        } else if current > target{
            j--
        } else {
            i++
        }
    }
    return false
}
