class Solution():
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r = 0
        c = 0
        row = 0
        index = 0
        column = 0

        while index < len(word) and row < len(board):
            if index == 0:
                column = 0
            r = row
            c = column
            while index < len(word) and column < len(board[row]):
                print(word[index], row, column)
                status = 0
                if board[row][column] == word[index]:
                    board[r][c] = 1
                    if (index + 1 >= len(word)):
                        return True
                    elif (c - 1 != -1) and (board[r][c - 1] != 1) and (board[r][c - 1] == word[index + 1]):
                        c = c - 1
                        index += 1
                        status = 1

                    elif (c + 1 < len(board[row])) and (board[r][c + 1] != 1) and (board[r][c + 1] == word[index + 1]):
                        c = c + 1
                        index += 1
                        status = 1

                    elif (r + 1 < len(board)) and (board[r + 1][c] != 1) and (board[r + 1][c] == word[index + 1]):
                        r = r + 1
                        index += 1
                        status = 1
                        break

                if status == 0:
                    index = 0
                    column += 1
                    c = column
                else:
                    column = c

            if row != r:
                row = r
            else:
                row += 1

        return False

obj = Solution()
print(obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
