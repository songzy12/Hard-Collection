class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        def cmp(x, y):
            if x + y < y + x: # NOTE: need to check both orders
                return -1
            if x + y > y + x:
                return 1
            return 0

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(cmp), reverse=True) # NOTE: reverse
        return str(int(''.join(nums))) # NOTE: strip leading 0