class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        res = 0

        while left <= right:
            mid = (left + right) // 2
            res = (mid / 2) * (mid + 1)

            if res > n:
                right = mid - 1
            else:
                left = mid + 1
        return right
