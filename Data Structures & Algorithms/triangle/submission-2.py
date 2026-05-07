class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        def dfs(r, c, cache):
            if (r,c) in cache:
                return cache[(r,c)]
            # if last row then return the min of the two below
            if r == (len(triangle) - 2):
                res = min(triangle[r+1][c], triangle[r+1][c+1]) + triangle[r][c]
                cache[(r,c)] = res
                return res
            
            res = min(dfs(r+1, c, cache), dfs(r+1, c+1, cache)) + triangle[r][c]
            cache[(r,c)] = res
            return res
        
        return dfs(0,0, {})
        