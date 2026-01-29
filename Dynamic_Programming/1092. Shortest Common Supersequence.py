class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = []

        for _ in range(len(str1)):
            inner_dp = [-1] * len(str2)
            dp.append(inner_dp)

        def recursion(word1_index, word2_idx, dp):
            if (word1_index == -1) or (word2_idx == -1):
                return 0
            
            if dp[word1_index][word2_idx] != -1:
                return dp[word1_index][word2_idx]
            
            if str1[word1_index] == str2[word2_idx]:
                dp[word1_index][word2_idx] = recursion(word1_index - 1, word2_idx - 1, dp) + 1

            else:
                dp[word1_index][word2_idx] = max(recursion(word1_index - 1, word2_idx, dp),recursion(word1_index, word2_idx - 1, dp))
                
                

            return dp[word1_index][word2_idx]
        
        lcs = recursion(len(str1) - 1, len(str2) - 1, dp)
        
        ans = ""
        print(lcs)

        row = len(str1) - 1
        column = len(str2) - 1

        while row >= 0 and column >= 0:
            if str1[row] == str2[column]:
                ans += str1[row]
                row -= 1
                column -= 1

            elif row > 0 and (dp[row - 1][column] >= dp[row][column - 1]):
                ans += str1[row]
                row -= 1

            else:
                ans += str2[column]
                column -= 1


        while (row >= 0): 
            ans += str1[row] 
            row -= 1 

        while (column >= 0 ): 
            ans += str2[column] 
            column -= 1 

        return ans[::-1]
