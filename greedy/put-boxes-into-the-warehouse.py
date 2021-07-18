"""
Let's think through an analogy first, that might be more relatable. Imagine that you are standing in front of a cave.
The cave goes down into the earth, becoming narrower and then wider in various places. 
Additionally, you have several stones in hand - of varying diameters. 
Your goal is to throw as many of the stones inside the cave as possible.
Let's think about the strategy you would use.

Firstly, if there is a bottleneck (a very narrow section) in the cave, then even if the cave becomes wider afterwards,
the stone will get stuck right before the bottleneck. So for each position in the cave, 
the largest stone that we can insert is limited by the narrowest part of the cave before it. 
In other words, that position's usable diameter is limited by the minimum diameter before it.

Secondly, throwing a small stone earlier is always better than throwing it later,
because if a small stone gets stuck, a larger stone will certainly get stuck, but the reverse is not true.

Therefore, our strategy would be to throw in the smallest stone first.

Now we can think of the stones as boxes, and the warehouse as the cave,
where the height of each warehouse room corresponds to the diameter of the cave.
The problem, and its solution, are now equivalent to the above analogy.
"""
class Solution(object):
    """
    Approach 2: Add Largest Possible Boxes from Left to Right
    
     For each position, we discard boxes that are too tall to fit in the current warehouse room, 
     because they won't fit in any rooms further to the right. 
     We put the tallest possible box that can fit in this room, and save the remaining boxes for warehouse rooms further 
     to the right.
    """
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        boxes.sort(reverse=True) # O(nlogn)
        result = 0
        for h in boxes:
            if h > warehouse[result]:
                continue
            result += 1
            if result == len(warehouse):
                break
        return result