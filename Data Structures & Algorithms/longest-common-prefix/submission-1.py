class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for idx in range(9999999):
            if idx >= len(strs[0]):
                return strs[0][0:idx]
            letter = strs[0][idx]
            for s in strs:
                if idx >= len(s):
                    return s[0:idx]
                
                if s[idx] != letter:
                    return s[0:idx]
            
                
            