class Solution:
    def mySqrt(self, x: int) -> int:

        if x is 0 or x is 1:
            return x
        left, right = 1, x
        mid = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
