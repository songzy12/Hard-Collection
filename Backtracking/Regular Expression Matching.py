class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = {}

        def get_dp(i, j):
            print(i, j)
            if i == len(s):
                for t in range(j, len(p), 2):
                    if t + 1 >= len(p) or p[t + 1] != '*':
                        return False
                return True # NOTE: do not forget this

            if j == len(p):
                return i == len(s)

            if (i, j) in dp:
                return dp[i, j]

            if j + 1 < len(p) and p[j + 1] == '*':
                if s[i] == p[j] or p[j] == '.':
                    dp[i, j] = get_dp(i, j + 2) or get_dp(i + 1, j)
                else:
                    # NOTE: j + 2 rather than j + 1
                    dp[i, j] = get_dp(i, j + 2)
            elif s[i] == p[j] or p[j] == '.':
                dp[i, j] = get_dp(i + 1, j + 1)
            else:
                dp[i, j] = False
            return dp[i, j]

        return get_dp(0, 0)


s = 'aa'
p = 'a*'

print(Solution().isMatch(s, p))
