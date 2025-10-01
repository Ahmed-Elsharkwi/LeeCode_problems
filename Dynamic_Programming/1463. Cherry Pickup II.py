class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(columns)]

        for r in reversed(range(rows)):
            cur = [[0] * columns for _ in range(columns)]

            for c_1 in range(columns - 1):
                for c_2 in range(c_1 + 1, columns):
                    max_cherries =  0
                    cherries =  grid[r][c_1] + grid[r][c_2]
                    
                    for cd_1 in [1, 0, -1]:
                        if c_1 - cd_1 >= 0:
                            for cd_2 in [1, 0, -1]:
                                if c_2 - cd_2 < columns:
                                    max_cherries = max(max_cherries, dp[c_1 - cd_1][c_2 - cd_2])
                    cur[c_1][c_2]  = max_cherries + cherries
            
            dp = cur
        return dp[0][columns - 1]
        
