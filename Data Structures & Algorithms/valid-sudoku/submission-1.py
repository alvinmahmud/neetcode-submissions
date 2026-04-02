class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for value in range(9):
                if board[row][value] == ".": continue
                if board[row][value] in seen: return False
                seen.add(board[row][value])
        
        for column in range(9):
            seen = set()
            for value in range(9):
                if board[value][column] == ".": continue
                if board[value][column] in seen: return False
                seen.add(board[value][column])
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".": continue
                    if board[row][col] in seen: return False
                    seen.add(board[row][col])
        
        return True