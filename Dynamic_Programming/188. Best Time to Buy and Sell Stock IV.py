class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = []

        for _ in range(n):
            inner_list = []
            for _ in range(2):
                inner_list_1 = [-1] * (k + 1)
                inner_list.append(inner_list_1)
            dp.append(inner_list)

        def recursion(index, state, cap, dp):
            if cap == 0:
                return 0
            if index == n:
                return 0
            
            if dp[index][state][cap] == -1:

                if state == 1:
                    dp[index][state][cap] = max(recursion(index + 1, 0, cap, dp)  - prices[index], recursion(index + 1, 1, cap, dp))
                else:
                    dp[index][state][cap] =  max(prices[index] + recursion(index + 1, 1, cap - 1, dp), recursion(index + 1, 0, cap, dp))
            
            return dp[index][state][cap]
        
        return recursion(0, 1, k , dp)
                
