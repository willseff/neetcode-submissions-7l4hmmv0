class Solution:
    def integerBreak(self, n: int) -> int:
        original_n = n
        def dfs(n, cache):
            #print("running dfs for n " + str(n))
            if n in cache:
                return cache[n]
            if n == 0:
                return 1
            if n == 1:
                return 1
            res = 0
            for i in range(1, n+1):
                #print("subtracting: " + str(i))
                if i == original_n:
                    continue
                res = max(res, i * dfs(n-i, cache))
                #print(res)
            cache[n] = res
            return res
        
        return dfs(n, {})


        