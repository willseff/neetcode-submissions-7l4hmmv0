class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, cache):
            if i in cache:
                return cache[i]
            #print(i)
            if i == 0:
                return 1

            res = 1
            curr = nums[i]

            # include ith index
            for j in range(i):
                if curr > nums[j]:
                     res = max(res, dfs(j, cache) + 1)
            
            cache[i] = res
            return res
        
        cache = {}
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, cache))

        return res
        


        

        