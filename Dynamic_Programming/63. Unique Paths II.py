class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        previous = [0] * len(obstacleGrid[0])

        for i in range(0, len(obstacleGrid)):
            temp = [0] * len(obstacleGrid[0])
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    if i == 0 and j == 0:
                        temp[j] = 1
                    elif j - 1 >= 0:
                        temp[j] = temp[j - 1] + previous[j]
                    else:
                        temp[j] = previous[j]
            previous = temp
        return previous[-1]
