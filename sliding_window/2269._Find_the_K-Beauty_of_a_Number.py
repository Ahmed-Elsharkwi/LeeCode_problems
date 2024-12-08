class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        left = 0
        count = 0

        for right in range(k - 1, len(num)):
            while (num[left] == 0 and left < right):
                left += 1
            print(int(num[left : right + 1]), count)
            if int(num[left : right + 1]) != 0:
                res = int(int(num) % int(num[left : right + 1]))
            if int(num[left : right + 1]) != 0 and res == 0:
                count += 1
            left += 1
        return count
