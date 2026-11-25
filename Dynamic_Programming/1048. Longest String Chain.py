class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def compare(str_1, str_2):
            if len(str_1) == len(str_2) + 1:
                first = 0
                second = 0

                while (first < len(str_1)):
                    if second < len(str_2) and str_1[first] == str_2[second]:
                        second += 1
                    
                    first += 1
                
                if (first == len(str_1)) and (second == len(str_2)):
                    return True
            
            return False
        
        words = sorted(words, key=len)
        dp = [1] * len(words)
        maxi = 0

        for i in range(0, len(words)):
            for j in range(0, i):
                if (compare(words[i], words[j])) and (dp[j] + 1 > dp[i]):
                    dp[i] = dp[j] + 1
            
            if dp[i] > maxi:
                maxi = dp[i]
        
        return maxi
                



                    
