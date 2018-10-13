class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # NOTE: otherwise TLE
        _p = ''
        for c in p:
            if c != '*':
                _p += c
            else:
                if not _p or _p and _p[-1] != '*':
                    _p += c
        p = _p

        dp = {}

        def get_dp(i, j):
            if i == len(s):
                for t in range(j, len(p)):
                    if p[t] != '*':
                        return False
            if j == len(p):
                return i == len(s)
            if (i, j) in dp:
                return dp[i, j]
            if p[j] == '?':
                dp[i, j] = get_dp(i + 1, j + 1)
            elif p[j] == '*':
                
                # for t in range(i, len(s)+1):
                #     if get_dp(t, j + 1):
                #         dp[i, j] = True
                #         break
                # else:
                #     dp[i, j] = False
                dp[i, j] = get_dp(i, j + 1) or get_dp(i + 1, j)
            else:
                dp[i, j] = (s[i] == p[j] and get_dp(i + 1, j + 1))
            return dp[i, j]
        return get_dp(0, 0)
