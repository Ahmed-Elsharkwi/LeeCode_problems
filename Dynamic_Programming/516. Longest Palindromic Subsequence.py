class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        reversed_str = s[::-1]
        prev = [0] * (len(reversed_str) + 1)

        for index in range(1, len(s) + 1):
            post = [0] * (len(reversed_str) + 1)

            for idx in range(1, len(reversed_str) + 1):
                if s[index - 1] == reversed_str[idx - 1]:
                    post[idx] = prev[idx - 1] + 1
                else:
                    post[idx] = max(prev[idx], post[idx - 1])
            prev = post
        
        return prev[-1]
