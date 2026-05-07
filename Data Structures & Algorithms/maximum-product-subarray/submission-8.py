import math
sys.setrecursionlimit(2000)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def dfs(L, R, cache):
            if (L, R) in cache:
                return cache[(L, R)]
            if L >= R:
                cache[(L, R)] = -99999999999
                return -99999999999

            currProd = math.prod(nums[L: R])

            cache[(L, R)] = max(currProd, dfs(L+1, R, cache), dfs(L, R-1, cache))
            return cache[(L, R)]

        return dfs(0, len(nums), {})




