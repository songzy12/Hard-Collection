class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right = [len(heights) for i in range(len(heights))]
        stack = []
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][-1]:
                stack.append([i, h])
            else:
                while stack and h < stack[-1][-1]:
                    index, height = stack.pop()
                    right[index] = i
                stack.append([i, h])

        left = [-1 for i in range(len(heights))]
        stack = []

        for _i, h in enumerate(heights[::-1]):
            i = len(heights) - 1 - _i
            if not stack or h >= stack[-1][-1]:
                stack.append([i, h])
            else:
                while stack and h < stack[-1][-1]:
                    index, height = stack.pop()
                    left[index] = i
                stack.append([i, h])

        res = 0
        for i, h in enumerate(heights):
            cur = h * (right[i] - left[i] - 1)
            res = max(res, cur)
        return res


# idea: for each index,
# find the left index and right index such all heights between are >=
