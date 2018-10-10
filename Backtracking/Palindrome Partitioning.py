# https://leetcode.com/explore/interview/card/top-interview-questions-hard/119/backtracking/852/


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        dp = {}

        def is_palindrome(i, j):
            if i >= j:
                return True
            if (i, j) in dp:
                return dp[i, j]
            if s[i] != s[j]:
                dp[i, j] = False
                return False
            return is_palindrome(i + 1, j - 1)

        dp_l = {}

        def _partition(i):
            if i in dp_l:
                return dp_l[i]
            res = []
            for t in range(i, len(s)):
                # print(i, t, s[i:t + 1])
                if is_palindrome(i, t):
                    _res = []
                    if t == len(s) - 1:
                        _res = [[s[i:t + 1]]]
                    else:
                        temp = _partition(t + 1)
                        # print(temp)
                        if temp:
                            _res = [[s[i:t + 1]] + x for x in temp]
                    res += _res
            # print(i, res)
            dp_l[i] = res
            return dp_l[i]
        # print(s)
        return _partition(0)


s = "aab"
print(Solution().partition(s))
