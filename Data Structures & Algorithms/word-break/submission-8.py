class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def mem(s, wordDict, cache):
            if s in cache:
                return cache[s]
            res = False
            for i in range(len(s)+1):
                if s[0:i] in wordDict:
                    if i < len(s):
                        res = res or mem(s[i:], wordDict, cache)
                        cache[s] = res
                    else:
                        cache[s] = True
                        return True
            return res
            
        return mem(s, wordDict, {})
        