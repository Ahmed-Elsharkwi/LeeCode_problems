class Solution:
    def minLength(self, s: str) -> int:
        char_stack = []
        index = -1

        for char in s:
            if (index != -1) and (
                (char == 'B' and char_stack[index] == 'A') or 
                (char == 'D' and char_stack[index] == 'C')):
                print(char_stack)
                char_stack.pop(index)
                index -= 1
            else:
                char_stack.append(char)
                index += 1
            
        return len(char_stack)
