class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(grid, r, c, visit):
            #print('current square: ' + str(r)+ " , "+ str(c))
            if (min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visit):
                #print('return 0')
                return 0

            visit.add((r,c))

            count = 1
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c-1, visit)
            count += dfs(grid, r, c+1, visit)

            return count
        
        visit = set()
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                print("i: "+ str(i) + " j: " + str(j))
                islandSize  = dfs(grid, i, j, visit)
                res = max(islandSize, res)
        
        return res

        
        