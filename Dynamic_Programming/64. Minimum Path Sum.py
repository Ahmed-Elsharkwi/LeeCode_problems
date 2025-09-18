class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prev = [99999999999999999] * m

        for i in range(0, n):
            temp = [0] * m

            for j in range(0, m):
                if (i == 0 and j == 0):
                    temp[j] = grid[i][j]
                elif (j == 0):
                    temp[j] = grid[i][j] + prev[j]
                else:
                    temp[j] = grid[i][j] + min(temp[j - 1], prev[j])
            prev = temp
        return prev[-1]


       
            
