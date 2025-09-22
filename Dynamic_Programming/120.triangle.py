class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = [] 
        sumition = 0

        for i in range(0, len(triangle)):
            temp = [99999999999999] * len(triangle[i])
            for j in range(0, len(triangle[i])):
                if i == 0 and j == 0:
                    temp[i] = triangle[i][j]
                elif j == 0:
                    temp[j] = triangle[i][j] + prev[j]
                else:
                    value = 9999999999999
                    if j != len(triangle[i - 1]):
                        value = prev[j]
                    temp[j] = triangle[i][j] + min(value, prev[j - 1])
            prev = temp
        return min(prev)
                
