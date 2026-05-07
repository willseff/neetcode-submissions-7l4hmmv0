class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(i, diff, cache):
            if (i, diff) in cache:
                return cache[(i, diff)]
            if i == len(nums)-1:
                if diff == nums[i] or diff == -nums[i]:
                    cache[(i, diff)] = True
                    return True
                else:
                    cache[(i, diff)] = False
                    return False
            
            assignNum = nums[i]
            cache[(i, diff)] = dfs(i + 1, diff + assignNum, cache) or dfs(i + 1, diff - assignNum, cache)
            return cache[(i, diff)]
            
        return dfs(0, 0, {})
            
            


        