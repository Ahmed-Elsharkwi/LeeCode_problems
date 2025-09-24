class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        prev = matrix[0]
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1, n):
            temp = [9999] * m

            for j in range(0, m):
                up_left = 9999
                up_right = 9999
                up = 9999

                if j - 1 >= 0:
                    up_left = prev[j - 1]
                if j + 1 < m:
                    up_right = prev[j + 1]

                up = prev[j]
                
                temp[j] = matrix[i][j] + min(up, up_left, up_right)
            
            prev = temp
        return (min(prev))
