class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        new_set = set()
        for letter in s:
            new_set.add(letter)

        for i in range(0, len(s)):
            if (s[i].lower() in new_set) and (s[i].upper() in new_set):
                continue
            else:
                sub_1 = self.longestNiceSubstring(s[0:i])
                sub_2 = self.longestNiceSubstring(s[i+1: ])
                if len(sub_1) >= len(sub_2):
                    return sub_1
                else:
                    return sub_2
        return s
