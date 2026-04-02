class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
                
            if (row, col) in visited or row == m or col == n or row < 0 or col < 0 or board[row][col] != word[i]:
                return False
            
            visited.add((row, col))

            if (dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1)):
                return True

            visited.remove((row, col))
 
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False