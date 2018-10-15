# https://leetcode.com/explore/interview/card/top-interview-questions-hard/120/sorting-and-searching/857/

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pass


# idea: totally no idea

# elements smaller than the 'median' are put into the last even slots
# elements larger than the 'median' are put into the first odd slots
# the medians are put into the remaining slots.

# https://conflatedthoughts.blogspot.com/2014/01/blum-floyd-pratt-rivest-tarjan-algorithm.html
# quick select to find median, quick select is like quick sort