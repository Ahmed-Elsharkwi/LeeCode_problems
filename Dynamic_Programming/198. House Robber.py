class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        db_array = [nums[0]]
        sum_1 = 0
        sum_2 = 0

        for i in range(1, len(nums)):
            if i - 2 >= 0:
                sum_1 = nums[i] + db_array[i - 2]
            else:
                sum_1 = nums[i]
            sum_2 = db_array[i - 1]

            db_array.append(max(sum_1, sum_2))
        return db_array[-1]
