class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        new_list = []
        if k > 0:
            for index in range(0, len(code)):
                idx = index + 1
                sum_1 = 0
                for count in range(0, k):
                    if idx == length:
                        idx = 0
                    sum_1 += code[idx]
                    idx += 1
                new_list.append(sum_1)
        elif k < 0:
            k = abs(k)
            for index in range(0, len(code)):
                idx = index - 1
                sum_1 = 0
                for count in range(0, k):
                    if idx == -1:
                        idx = length - 1
                    sum_1 += code[idx]
                    idx -= 1
                new_list.append(sum_1)
        else:
            for index in range(0, len(code)):
                new_list.append(0)
        return new_list
