class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        hash_number_letters = {
            "1": [], 
            "2": ['a', 'b', 'c'], 
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        new_list = []

        def collect_possibilities(index, prev_charcater):
            if index == len(digits) - 1:
                for letter in (hash_number_letters[digits[index]]):
                    new_list.append(prev_charcater + letter)
                
                return
            
            for letter in (hash_number_letters[digits[index]]):
                collect_possibilities(index + 1, letter)
                for idx in range(0, len(new_list)):
                    
                    if len(new_list[idx]) <= (len(digits) - index):
                        new_list[idx] = prev_charcater + new_list[idx]

        collect_possibilities(0, "")
        return new_list
