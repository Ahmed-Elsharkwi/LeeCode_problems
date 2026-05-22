class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            cur = [0] * (n + 1)
            for j in range(i, -1, -1):
                len_1 = prev[j]
                len_2 = 0

                if (j == 0) or (nums[i] > nums[j - 1]):
                    len_2 = 1 + prev[i + 1]
                
                cur[j] = max(len_1, len_2)
            
            prev = cur
        
        return prev[0]
