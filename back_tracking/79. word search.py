class Solution:
    def exist(self, board, word):
        rows = len(board)
        columns = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if ((c < 0) or 
                (r < 0) or
                (c >= columns) or
                (r >= rows) or
                ((r, c) in path) or
                board[r][c] != word[i]):
                return False
            
            path.add((r, c))
            result = (dfs(r + 1, c, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return result
        
        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        return False
