class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPalindromeLeft(s):
            L, R = 0, len(s) - 1
            letter_skipped = False
            while L < R:
                print("L " + str(s[L]), 'R ' + str(s[R]))
                if s[L] == s[R]:
                    L += 1
                    R -= 1
                    continue
                else:
                    if letter_skipped:
                        print("L, R = " + str(L)+ " " + str(R))
                        return False
                    elif s[L+1] == s[R]:
                        print("Left Letter skipped L, R = " + str(L)+ " " + str(R))
                        L += 1
                        letter_skipped = True
                        continue
                    elif s[L] == s[R -1]:
                        print("Right Letter skipped L, R = " + str(L)+ " " + str(R))
                        R -= 1
                        letter_skipped = True
                        continue
                    else:
                        return False
            return True
        def validPalindromeRight(s):
            L, R = 0, len(s) - 1
            letter_skipped = False
            while L < R:
                print("L " + str(s[L]), 'R ' + str(s[R]))
                if s[L] == s[R]:
                    L += 1
                    R -= 1
                    continue
                else:
                    if letter_skipped:
                        print("L, R = " + str(L)+ " " + str(R))
                        return False
                    elif s[L] == s[R -1]:
                        print("Right Letter skipped L, R = " + str(L)+ " " + str(R))
                        R -= 1
                        letter_skipped = True
                        continue
                    elif s[L+1] == s[R]:
                        print("Left Letter skipped L, R = " + str(L)+ " " + str(R))
                        L += 1
                        letter_skipped = True
                        continue
                    else:
                        return False
            return True
        
        return validPalindromeRight(s) or validPalindromeLeft(s)


        