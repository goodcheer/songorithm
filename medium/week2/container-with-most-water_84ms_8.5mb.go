func MaxOf(a int, b int) int {
    max := a
    if a < b {
        max = b
    }
    return max
}

func maxArea(height []int) int {
    var begin, area, t int = 0, 0, 0
    var end int = len(height) - 1
    
    for begin != end {
        if height[begin]  < height[end] {
            t = height[begin] * (end - begin)
            area = MaxOf(area, t)
            begin++
        } else {
            t = height[end] * (end - begin)
            area = MaxOf(area, t)
            end--
        }
    }
    return area
}
