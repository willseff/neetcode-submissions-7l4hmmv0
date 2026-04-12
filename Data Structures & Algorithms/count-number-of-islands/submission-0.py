class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return

            if grid[r][c] == "1":
                print("update " + str(r) + " , " + str(c) + " to zero")
                grid[r][c] = "0"

                dfs(grid, r + 1, c)
                dfs(grid, r - 1, c)
                dfs(grid, r, c + 1)
                dfs(grid, r, c - 1)
            
            return
        


        # i = row
        # j = col
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print("grid value: " + str(grid[i][j]))
                if grid[i][j] == "1":
                    print("island found")
                    res += 1
                    dfs(grid, i, j)
        
        return res


        