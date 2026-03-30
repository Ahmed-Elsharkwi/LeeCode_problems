class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next = [0] * 2
        n = len(prices)

        for i in range(n - 1, -1, -1):
            cur = [0] * 2

            for j in range(0, 2):
                if j == 0:
                    cur[j] = max((next[1] - prices[i]), next[0])
                else:
                    cur[j] = max((prices[i] + next[0]), next[1])
            
            next = cur
        
        return next[0]
            
