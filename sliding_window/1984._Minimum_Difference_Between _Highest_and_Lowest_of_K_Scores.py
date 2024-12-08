class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        num = nums[k - 1] - nums[left]
        for right in range(k, len(nums)):
            left += 1
            num = min(num, nums[right] - nums[left])
        return num
