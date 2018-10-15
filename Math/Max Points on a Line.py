# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        pass

# idea: for each of the points, 
# count how many points are on the same line
# time complexity: O(n^3)

# for each node, compute the slope of nodes behind
# then use a map to store the slopes

# be careful with same points and infinite slope