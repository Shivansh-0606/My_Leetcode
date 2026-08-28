class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n) ]
        
        cols = set()
        posdiag = set() # r+c = const
        negdiag = set() # r-c = const

        def backtrack(r:int):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in posdiag or (r-c)  in negdiag:
                    continue
                
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)

                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res