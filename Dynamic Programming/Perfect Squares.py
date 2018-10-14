class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        def get_dp(t):
            if t in dp:
                return dp[t]
            if t == 0:
                return t
            
            res = t
            for i in range(1, int(t**0.5) + 1):
                res = min(res, 1 + get_dp(t - i*i))
            dp[t] = res
            return res
        return get_dp(n)
