class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            # true = surrounded
            if min(r,c) < 0 or r == ROWS or c == COLS:
                return False
            
            if grid[r][c]== 'X' or (r,c) in visit:
                return True

            visit.add((r,c))
            
            surrounded = dfs(grid, r + 1, c, visit) and dfs(grid, r - 1, c, visit) and dfs(grid, r, c + 1, visit) and dfs(grid, r, c - 1, visit)

            visit.remove((r,c))
            # if surrounded:
            #     grid[r][c] = 'X'
            
            return surrounded

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, set()):
                    board[i][j] = 'X'         

        #return board      



