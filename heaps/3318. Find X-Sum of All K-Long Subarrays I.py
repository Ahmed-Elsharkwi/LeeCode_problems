class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answers = []
        number = (len(nums) - k) + 1

        for i in range(0, number):
            new_dict = {}
            new_list = nums[i : (i + k)]
            

            for element in new_list:
                if element in new_dict:
                    new_dict[element] += 1
                else:
                    new_dict[element] = 1
            
            total = 0
            
            for l in range(0, x):
                frequ = 0
                tmp_key = 0
                for key, value in new_dict.items():
                    if (value > frequ) or (value == frequ and key > tmp_key):
                        frequ = value
                        tmp_key = key
                if len(new_dict) != 0:
                    total += new_dict[tmp_key] * tmp_key
                    del new_dict[tmp_key]
            

            answers.append(total)

        return answers

                
                    

