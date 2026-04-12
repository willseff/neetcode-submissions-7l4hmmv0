class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, n = -1, len(s)
        max_string = ''
        dp = [[False]* n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                #print("coordinates: " + str(i) + " : " + str(j))
                if (j-i < 2 and (s[i] == s[j])):
                    dp[i][j] = True
                    if j - i > max_len:
                        max_string = s[i:j+1]
                        #print(max_string)
                        max_len = j - i 

                elif ((s[i] == s[j]) and (dp[i+1][j-1])):
                    dp[i][j] = True
                    if j - i > max_len:
                        max_string = s[i:j+1]
                        #print(max_string)
                        max_len = j - i 

        #print(dp)
        return max_string
            

        