class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = (sum(nums[:k])) / k

        sum_1 = sum(nums[0:k])
        left = 0

        for right in range(k, len(nums)):
            sum_1 = (sum_1 - nums[left]) + nums[right]
            avr = sum_1 / k
            left += 1
            average = max(average, avr)
        return average 
            
