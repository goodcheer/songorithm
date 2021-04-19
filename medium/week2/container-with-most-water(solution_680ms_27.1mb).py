from collections import defaultdict

class Solution:
    """
    begin and end are the coordinates of the list, it changes at every iteration based on specified condition.

    At initial state, if list of height = [1,8,6,2,5,4,8,3,7], the coordinates of begin and end is 0 and 8 (length of list -1) respectively.
    Since the area is calculated using minimum of height at those two coordinates, we need to know which coordinate has the smaller height,
    then calculate the area accordingly using that smaller height. After each iteration, move the coordinate that has the smaller height closer
    to the other end.

    Do that for every iteration until begin and end meets. This is checked by "while begin != end". 
    The max area is checked and stored at every iteration, then returned at the end of the function.
    """
    def maxArea(self, height: List[int]) -> int:
        begin, end = 0, len(height) - 1
        area = 0
        while begin != end:
            if height[begin] < height[end]:
                t = height[begin]*(end - begin)
                area = max(area,t)
                begin += 1
            else:
                t = (height[end]*(end - begin))
                area = max(area,t)
                end -= 1

        return area
