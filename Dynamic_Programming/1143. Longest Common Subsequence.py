class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(idx_t1, idx_t2):
            if (idx_t1 == -1) or (idx_t2 == -1):
                return 0
            
            if dp[idx_t1][idx_t2] == -1:
                if text1[idx_t1] == text2[idx_t2]:
                    dp[idx_t1][idx_t2] = rec(idx_t1 - 1, idx_t2 - 1) + 1
                else:
                    dp[idx_t1][idx_t2] = max(rec(idx_t1 - 1, idx_t2), rec(idx_t1, idx_t2 - 1))

            return dp[idx_t1][idx_t2]
        
        length_t1 = len(text1)
        length_t2 = len(text2)

        dp = []
        for _ in range(length_t1):
            inner_list = [-1] * length_t2
            dp.append(inner_list)

        return rec(length_t1 - 1, length_t2 - 1)
        
