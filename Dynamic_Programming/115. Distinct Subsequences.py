class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = []

        for _ in range(len(s)):
            dp.append([-1] * len(t))
            
        def rec(i, j, dp):
            if j < 0:
                return 1
            if i < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            else:
                if s[i] == t[j]:
                    dp[i][j] = rec(i - 1, j - 1, dp) + rec(i - 1, j, dp)
                else:
                    dp[i][j] = rec(i - 1, j, dp)
            
            return dp[i][j]
        
        return rec(len(s) - 1, len(t) - 1, dp)
