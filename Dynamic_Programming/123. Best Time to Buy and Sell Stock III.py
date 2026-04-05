class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next = [[0] * 3 for _ in range(2)]
        n = len(prices)

        for i in range(n - 1, -1, -1):
            cur =  [[0] * 3 for _ in range(2)]

            for j in range(0, 2):            
                for n in range(1, 3):
                    if j == 0:
                        cur[j][n] = max((next[1][n] - prices[i]), next[0][n])
                    else:
                        cur[j][n] = max((prices[i] + next[0][n - 1]), next[1][n])

                
            
            next = cur
        
        return next[0][2]
            
