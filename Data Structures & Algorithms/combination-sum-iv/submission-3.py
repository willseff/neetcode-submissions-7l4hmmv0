class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1

        def dfs(target, cache):
            if target in cache:
                return cache[target]

            res = 0
            for num in nums:
                if target == num:
                    res += 1
                elif target > num:
                    res += dfs(target-num, cache)
            
            cache[target] = res
            return res
        
        return dfs(target, {})
        