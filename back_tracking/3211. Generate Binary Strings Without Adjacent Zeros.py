class Solution:
    def validStrings(self, n):
        new_list = []

        def collect_possibilites(i, string):
            if i == n:
                new_list.append(string)
                return
            
            if string == "" or string[-1] != '0':
                collect_possibilites(i + 1, string + '0')

            collect_possibilites(i + 1, string + '1')
        
        collect_possibilites(0, "")
        return new_list

