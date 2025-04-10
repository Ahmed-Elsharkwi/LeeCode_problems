class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(nums_list, duplicates):
            if len(nums_list) == 1:
                result.append(nums_list)
                return

            for index in range(len(nums_list)):
                if nums_list[index] not in duplicates:
                    duplicates.append(nums_list[index])
                    new_nums = nums_list.copy()
                    new_nums.pop(index)
                    
                    backtracking(new_nums, [])

                    for inner_list in result:
                        if len(inner_list) < len(nums_list):
                            inner_list.append(nums_list[index])
        
        backtracking(nums.copy(), [])
        return result
                            
