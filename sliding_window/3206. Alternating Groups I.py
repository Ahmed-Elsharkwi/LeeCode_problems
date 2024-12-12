class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        right = 3 - 1
        mid = right - 1
        count = 0

        for left in range(0, len(colors)):
            if right == len(colors):
                right = 0
            if colors[mid] != colors[right] and colors[mid] != colors[left]:
                count += 1
            mid = right
            right += 1
        return count
