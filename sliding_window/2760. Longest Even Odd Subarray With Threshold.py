class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        left = 0
        i = 0
        flag = False
        indcat = 0

        for right in range(0, len(nums)):
            i = left
            if nums[left] % 2 == 0:
                while (i <= right):
                    if nums[i] > threshold:
                        flag = False
                        break 
                    if (i != right) and (nums[i] % 2) == (nums[i + 1] % 2):
                        flag = False
                        break
                    flag = True
                    i += 1
                if flag is True:
                    indcat = max(indcat, (right - left + 1))
            if flag is False:
                left += 1
        return indcat
