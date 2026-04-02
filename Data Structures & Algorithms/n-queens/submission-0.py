class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        add_diag = set()
        sub_diag = set()
        board = [['.'] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in add_diag or (r - c) in sub_diag:
                    continue
                
                cols.add(c)
                add_diag.add(r + c)
                sub_diag.add(r - c)
                board[r][c] = 'Q'

                dfs(r + 1)

                cols.remove(c)
                add_diag.remove(r + c)
                sub_diag.remove(r - c)
                board[r][c] = '.'
        
        dfs(0)
        return res
