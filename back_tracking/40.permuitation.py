class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outer_list = []
        length = len(nums)

        def backtracking(nums_list):
            if len(nums_list) == 1:
                outer_list.append(nums_list)
                return
            
            for index in range(0, len(nums_list)):
                new_list = nums_list.copy()
                new_list.pop(index)

                backtracking(new_list)

                for inner_list in outer_list:
                    if len(inner_list) < len(nums_list):
                        inner_list.append(nums_list[index])

        backtracking(nums.copy())
        return outer_list
