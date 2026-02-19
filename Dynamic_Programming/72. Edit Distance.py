class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        first_list = []

        for j in range(0, len(word2) + 1):
            first_list.append(j)
        
        for i in range(1, len(word1) + 1):
            second_list = [0] * (len(word2) + 1)
            second_list[0] = i

            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    second_list[j] = first_list[j - 1]
                else:
                    second_list[j] = 1 + min((second_list[j - 1]), min((first_list[j]), (first_list[j - 1])))
            
            first_list = second_list
        
        return first_list[len(word2)]
