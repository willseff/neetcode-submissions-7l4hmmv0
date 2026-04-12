class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs_pacific(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) == 0:
                return True
            elif r == ROWS or c == COLS or (r, c) in visit: 
                return False
            
            visit.add((r, c))

            current_height = grid[r][c]
            #print("coordinates: " + str(r) + " : " + str(c))
            if (r + 1) < ROWS:
                up = dfs_pacific(grid, r + 1, c, visit) if ((grid[r + 1][c] <= current_height)) else False
            else:
                up = False
            down = dfs_pacific(grid, r - 1, c, visit) if grid[r -1 ][c] <= current_height else False
            left = dfs_pacific(grid, r, c - 1, visit) if grid[r][c - 1] <= current_height else False
            if c + 1 < COLS:
                right = dfs_pacific(grid, r, c + 1, visit) if (grid[r][c + 1] <= current_height) else False
            else:
                right = False

            return up or down or left or right

        def dfs_atlantic(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if r == (ROWS - 1) or c == (COLS - 1):
                return True
            elif (r, c) in visit: 
                return False
            
            visit.add((r, c))

            current_height = grid[r][c]
            #print("coordinates: " + str(r) + " : " + str(c))
            if (r + 1) < ROWS:
                up = dfs_atlantic(grid, r + 1, c, visit) if ((grid[r + 1][c] <= current_height)) else False
            else:
                up = False
            if (r > 0):
                down = dfs_atlantic(grid, r - 1, c, visit) if grid[r -1 ][c] <= current_height else False
            else:
                down = False
            if (c > 0):
                left = dfs_atlantic(grid, r, c - 1, visit) if grid[r][c - 1] <= current_height else False
            else:
                left = False
            if c + 1 < COLS:
                right = dfs_atlantic(grid, r, c + 1, visit) if (grid[r][c + 1] <= current_height) else False
            else:
                right = False

            return up or down or left or right

        pacific_list = []
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if dfs_pacific(heights, r, c, set()) and dfs_atlantic(heights, r, c, set()):
                    res.append([r, c])
                # if dfs_atlantic(heights, r, c, set()):
                #     res.append([r, c])
        
        return res




        