class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []

        for _ in range(len(word1)):
            inner_dp = [-1] * len(word2)
            dp.append(inner_dp)

        def recursion(word1_index, word2_idx, dp):
            if (word1_index == -1) or (word2_idx == -1):
                return 0
            
            if dp[word1_index][word2_idx] != -1:
                return dp[word1_index][word2_idx]
            
            if word1[word1_index] == word2[word2_idx]:
                dp[word1_index][word2_idx] = recursion(word1_index - 1, word2_idx - 1, dp) + 1

            else:
                dp[word1_index][word2_idx] = max(recursion(word1_index - 1, word2_idx, dp), recursion(word1_index, word2_idx - 1, dp))
            return dp[word1_index][word2_idx]
        
        lcs = recursion(len(word1) - 1, len(word2) - 1, dp)

        deletion_opt_word_1 = len(word1) - lcs
        deletion_opt_word_2 = len(word2) - lcs

        return deletion_opt_word_1 + deletion_opt_word_2
