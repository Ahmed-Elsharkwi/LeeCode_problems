class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = []
        for _ in range(m + 1):
            new_list = []
            for _ in range(n + 1):
                new_list.append(None)
            memo.append(new_list)

        memo[0][0] = 1

        for row in range(0, m):

            for column in range(0, n):
                if row == 0 and column == 0:
                    continue
                left = 0
                up = 0
                if column - 1 >= 0: 
                    left = memo[row][column - 1]
                if row - 1 >= 0: 
                    up = memo[row - 1][column]
              
                memo[row][column] = up + left
        
        return memo[m - 1][n - 1]

