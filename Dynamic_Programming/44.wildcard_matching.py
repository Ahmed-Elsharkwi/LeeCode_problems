class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev = [False] * (len(s) + 1)
        prev[0] = True

        for i in range(1, len(p) + 1):
            cur = [False] * (len(s) + 1)
            flag = True

            for u in range(0, i):
                if p[u] != '*':
                    flag = False
                    break
            
            cur[0] = flag

            for j in range(1, len(s) + 1):
                if (p[i - 1] == s[j - 1]) or (p[i - 1] == '?'):
                    cur[j] = prev[j - 1]
                elif p[i - 1] == '*':
                    cur[j] = prev[j] | cur[j - 1]
                else:
                    cur[j] = False
            
            prev = cur
        
        return prev[len(s)]
