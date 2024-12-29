# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        bad_version = None

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) is True:
                right = mid - 1
                bad_version = mid
            else:
                left = mid + 1
        return bad_version
