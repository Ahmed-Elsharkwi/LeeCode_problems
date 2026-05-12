class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prev = [0] * 2
        
        for i in range(len(prices) - 1, -1, -1):
            current = [0] * 2
            for j in range(0, 2):
                if j == 0:
                    current[j] = max((prev[1] - prices[i]), prev[0])
                else:
                    current[j] = max(((prev[0] + prices[i]) - fee ), prev[1])
            
            prev =  current
        
        return prev[0]

