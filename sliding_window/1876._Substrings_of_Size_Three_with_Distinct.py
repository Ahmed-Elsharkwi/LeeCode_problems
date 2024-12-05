class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        a, b, c = s[0], s[1], s[2]
        res = 0

        for i in range(3, len(s) + 1):
            if a != b and b != c and c != a:
                res += 1
            a = b
            b = c
            if i != len(s):
                c = s[i]
        return res
        
