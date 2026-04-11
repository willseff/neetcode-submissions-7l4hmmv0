class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        dp = [[False] * n for _ in range(n)]
        
        for i in range(n, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                    res += 1
                    continue
                if (j - i) == 1:
                    if(s[i] == s[j]):
                        dp[i][j] = True
                        res += 1
                    continue
                ends_match = (s[i] == s[j])
                if ends_match and dp[i+1][j-1]:
                    dp[i][j] = True
                    res += 1
        return res