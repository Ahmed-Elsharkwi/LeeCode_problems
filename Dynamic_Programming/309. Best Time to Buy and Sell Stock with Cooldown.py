class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = []

        for _ in range(n):
            inner_list = []
            
            dp.append([-1] * 2)

        def recursion(index, state, dp):
            if index >= n:
                return 0
            
            if dp[index][state] == -1:

                if state == 1:
                    dp[index][state] = max(recursion(index + 1, 0, dp)  - prices[index], recursion(index + 1, 1, dp))
                else:
                    dp[index][state] =  max(prices[index] + recursion(index + 2, 1, dp), recursion(index + 1, 0, dp))
            
            return dp[index][state]
        
        return recursion(0, 1, dp)
