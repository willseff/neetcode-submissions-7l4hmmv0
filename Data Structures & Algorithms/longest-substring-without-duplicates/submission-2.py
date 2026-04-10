class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        curr_set = set()
        L = 0

        for R in range(len(s)):
            if s[R] not in curr_set:
                curr_set.add(s[R])
                res = max(res, R - L + 1)
                print(curr_set)
            # when s[R] is in the set we remove L items until we remove the same    
            else:
                print('this is in the set')
                while s[L] != s[R]:
                    curr_set.discard(s[L])
                    L += 1
                L += 1
        
        return res
