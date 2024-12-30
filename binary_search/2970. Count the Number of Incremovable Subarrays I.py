class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        counter = 0
        for index in range(0, len(nums)):
            for i in range(index, len(nums)):
                new_list = []
                for i in range(index, i + 1):
                    new_list.append(i)
                num = 0
                flag = False
                for idx in range(0, len(nums)):
                    if idx in new_list:
                        continue
                    else:
                        if nums[idx] > num:
                            num = nums[idx]
                            flag = True
                        else:
                            flag = False
                            break
                
                if flag is True:
                    counter += 1
        return counter + 1
